import logging
import os

def setup_logger(test_name):
    """Set up a logger for the given test."""
    os.makedirs("logs", exist_ok=True)  # Ensure logs directory exists
    log_file = os.path.join("logs", f"{test_name}.log")

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, mode="w")
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
