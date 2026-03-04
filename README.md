# Qwen3.5-0.8B CPU Chat Space

This Hugging Face Space provides a ChatGPT-like interface for the Qwen3.5-0.8B model running entirely on CPU. It's designed to work on free CPU-based instances without requiring GPU acceleration.

## Features

- ChatGPT-like chat interface with streaming token output
- Adjustable parameters: temperature, top_p, max_new_tokens, repetition_penalty
- "Thinking mode" toggle for enhanced reasoning capabilities
- System prompt support
- Conversation history management with truncation to prevent overload
- Stop generation functionality
- Automatic model download and caching

## How It Works

The application uses the Hugging Face Transformers library with the Qwen3.5-0.8B model. On first run, the model is automatically downloaded and cached. The interface is built with Gradio, providing a web-based chat experience.

The model runs entirely on CPU with optimized settings:
- `device_map="cpu"`
- `torch_dtype=torch.float32`
- `low_cpu_mem_usage=True`

## CPU Limitations

- First run will be slower due to model download and initial loading
- Response times may be slower compared to GPU inference
- Large conversations may impact performance, so history is automatically truncated

## Changing the Model

To use a different model, modify the `MODEL_NAME` variable in `app.py` to point to another Hugging Face model ID.

## First Run Considerations

The first time you run this space, it will automatically download the Qwen3.5-0.8B model (~2.3GB). This may take several minutes depending on the network speed. Subsequent runs will use the cached model.

## Requirements

- Python 3.8+
- PyTorch
- Transformers >= 4.45.0
- Gradio >= 4.0.0
