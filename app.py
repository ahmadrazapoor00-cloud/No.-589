import os
import gc
import threading
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer
import gradio as gr
import time

# Set up cache directories if /data exists
if os.path.exists("/data"):
    hf_home = "/data/hf"
    os.makedirs(hf_home, exist_ok=True)
    os.environ["HF_HOME"] = hf_home
    os.environ["TRANSFORMERS_CACHE"] = f"{hf_home}/transformers"
    os.environ["HF_HUB_CACHE"] = f"{hf_home}/hub"

# Model configuration
MODEL_NAME = "Qwen/Qwen3.5-0.8B"

# Initialize model and tokenizer globally
tokenizer = None
model = None

def initialize_model():
    global tokenizer, model
    if tokenizer is None or model is None:
        print("Loading model...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            device_map="cpu",
            torch_dtype=torch.float32,
            low_cpu_mem_usage=True
        )
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.eos_token_id
        print("Model loaded successfully.")

# Global stop generation flag
stop_signal = threading.Event()

def format_history_for_token_count(history):
    """Format history for rough token estimation"""
    formatted = ""
    for role, msg in history:
        if msg:
            formatted += f"{role}: {msg}\n"
    return formatted

def count_approximate_tokens(text):
    """Roughly estimate token count (1 token ~ 4 chars for English)"""
    return len(text.encode('utf-8')) // 4

def truncate_history(history, max_turns=12, max_tokens=2048):
    """Truncate history to prevent overload"""
    # First, limit by number of turns
    if len(history) > max_turns * 2:  # Each turn is user+assistant
        history = history[-max_turns*2:]
    
    # Then check token count
    formatted_text = format_history_for_token_count(history)
    token_count = count_approximate_tokens(formatted_text)
    
    while token_count > max_tokens and len(history) > 2:
        # Remove oldest pair (user + assistant)
        history = history[2:]
        formatted_text = format_history_for_token_count(history)
        token_count = count_approximate_tokens(formatted_text)
    
    return history

def generate_response(history, system_prompt, temperature, top_p, max_new_tokens, repetition_penalty, thinking_mode):
    # Initialize model if not already done
    initialize_model()
    
    # Truncate history to prevent overload
    history = truncate_history(history)
    
    # Prepare messages for chat template
    messages = []
    if system_prompt.strip():
        messages.append({"role": "system", "content": system_prompt})
    
    for i, (role, content) in enumerate(history):
        if content:  # Only add non-empty messages
            messages.append({"role": role, "content": content})
    
    # Add user role for the latest message if not already present
    if history and history[-1][0] == "user":
        pass  # Already handled above
    else:
        # This case shouldn't happen during streaming, but just in case
        pass
    
    # Apply chat template
    try:
        if thinking_mode:
            # Try to apply thinking mode - handle gracefully if not supported
            try:
                chat_template_kwargs = {"enable_thinking": True}
                text = tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True,
                    chat_template_kwargs=chat_template_kwargs
                )
            except TypeError:
                # Fallback if chat_template_kwargs not supported
                text = tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True
                )
        else:
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
    except Exception:
        # General fallback
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
    
    # Tokenize input
    inputs = tokenizer([text], return_tensors="pt")
    
    # Clear stop signal
    stop_signal.clear()
    
    # Create streamer and generate in background thread
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    
    generation_kwargs = {
        "input_ids": inputs["input_ids"],
        "attention_mask": inputs["attention_mask"],
        "streamer": streamer,
        "max_new_tokens": max_new_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "repetition_penalty": repetition_penalty,
        "do_sample": True,
        "pad_token_id": tokenizer.eos_token_id
    }
    
    def generate_and_signal():
        try:
            model.generate(**generation_kwargs)
        except Exception as e:
            print(f"Generation error: {e}")
        finally:
            # Signal completion
            stop_signal.set()
    
    thread = threading.Thread(target=generate_and_signal)
    thread.start()
    
    # Yield tokens as they become available
    generated_text = ""
    for new_text in streamer:
        if stop_signal.is_set():
            break
        generated_text += new_text
        yield generated_text
    
    # Wait for thread to finish
    thread.join()
    
    # Clear CUDA cache if available (though we're using CPU, good practice)
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    gc.collect()

def clear_chat():
    return []

def stop_generation():
    stop_signal.set()
    return "Generation stopped."

with gr.Blocks(title="Qwen3.5-0.8B CPU Chat") as demo:
    gr.Markdown("# Qwen3.5-0.8B CPU Chat")
    gr.Markdown("Chat with Qwen3.5-0.8B model running entirely on CPU.")
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                label="Conversation",
                bubble_full_width=False,
                height=500
            )
            user_input = gr.Textbox(
                label="Your Message",
                placeholder="Type your message here...",
                lines=3
            )
            
            with gr.Row():
                submit_btn = gr.Button("Send", variant="primary")
                clear_btn = gr.Button("Clear Chat")
                
        with gr.Column(scale=1):
            gr.Markdown("### Settings")
            system_prompt = gr.Textbox(
                label="System Prompt (Optional)",
                placeholder="Enter system instructions...",
                lines=3
            )
            temperature = gr.Slider(0.2, 1.2, value=0.7, label="Temperature")
            top_p = gr.Slider(0.1, 1.0, value=0.9, label="Top-p")
            max_new_tokens = gr.Slider(32, 1024, value=384, step=32, label="Max New Tokens")
            repetition_penalty = gr.Slider(1.0, 2.0, value=1.1, label="Repetition Penalty")
            thinking_mode = gr.Checkbox(label="Enable Thinking Mode")
            stop_btn = gr.Button("Stop Generation")
    
    # Event handling
    submit_btn.click(
        fn=lambda history, message: history + [(message, None)],
        inputs=[chatbot, user_input],
        outputs=[chatbot]
    ).then(
        fn=generate_response,
        inputs=[
            chatbot, system_prompt, temperature, top_p, 
            max_new_tokens, repetition_penalty, thinking_mode
        ],
        outputs=[chatbot],
        show_progress=False
    )
    
    user_input.submit(
        fn=lambda history, message: history + [(message, None)],
        inputs=[chatbot, user_input],
        outputs=[chatbot]
    ).then(
        fn=generate_response,
        inputs=[
            chatbot, system_prompt, temperature, top_p, 
            max_new_tokens, repetition_penalty, thinking_mode
        ],
        outputs=[chatbot],
        show_progress=False
    )
    
    clear_btn.click(
        fn=clear_chat,
        inputs=None,
        outputs=[chatbot]
    )
    
    stop_btn.click(
        fn=stop_generation,
        inputs=None,
        outputs=[gr.Textbox(visible=False)]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)