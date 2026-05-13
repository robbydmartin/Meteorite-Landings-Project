import logging
from logging import handlers
from logging.handlers import RotatingFileHandler
from pathlib import Path

MAX_BYTES = 5 * 1024 * 1024

def setup_logging() -> logging.Logger:

    # Create path to log file
    project_root = Path(__file__).resolve().parents[2]
    log_dir = project_root / "data"/ "logs"

    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "meteorite_landings_data_ingestion.log"

    # Create logging instance.
    logger = logging.getLogger()

    # Check if logger has handlers to avoid creating multiple instances.
    if logger.handlers:
        return logger
    
    # Set logging level.
    logger.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter("%(asctime)s | %(levelname)s | %(module)s | %(lineno)s | %(message)s")
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    # File handler
    file_handler = RotatingFileHandler(log_file, mode="a", maxBytes=MAX_BYTES, backupCount=1)
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(module)s | %(lineno)s | %(message)s")
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    return logger