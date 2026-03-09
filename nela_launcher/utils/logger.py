"""
Nela Launcher Logger
Setup and configure application logging
"""

import logging
from pathlib import Path
from datetime import datetime


def setup_logger(log_dir: str = "logs", level: int = logging.INFO) -> logging.Logger:
    """
    Setup and configure the application logger
    
    Args:
        log_dir: Directory to store log files
        level: Logging level
        
    Returns:
        Configured logger instance
    """
    
    # Create logs directory
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)
    
    # Create logger
    logger = logging.getLogger("nela_launcher")
    logger.setLevel(level)
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler - current session
    session_log = log_path / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(session_log, encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # File handler - latest (always updated)
    latest_log = log_path / "latest.log"
    latest_handler = logging.FileHandler(latest_log, encoding='utf-8', mode='w')
    latest_handler.setLevel(level)
    latest_handler.setFormatter(formatter)
    logger.addHandler(latest_handler)
    
    return logger


def get_logger(name: str = "nela_launcher") -> logging.Logger:
    """
    Get a logger instance
    
    Args:
        name: Logger name
        
    Returns:
        Logger instance
    """
    return logging.getLogger(name)
