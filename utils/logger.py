"""Logging configuration for the test automation framework."""

import os
import sys
from pathlib import Path
from loguru import logger

# Create logs directory if it doesn't exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Log file paths
LOG_FILE = LOG_DIR / "test_automation.log"
ERROR_FILE = LOG_DIR / "error.log"

# Configure loguru
logger.remove()  # Remove default handler

# Console logging
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level=os.getenv("LOG_LEVEL", "INFO"),
    colorize=True,
)

# File logging - all levels
logger.add(
    str(LOG_FILE),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="500 MB",
    retention="7 days",
)

# File logging - errors only
logger.add(
    str(ERROR_FILE),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="ERROR",
    rotation="500 MB",
    retention="30 days",
)


def get_logger(name: str):
    """Get a logger instance with the given name."""
    return logger.bind(name=name)
