import logging
from logging.handlers import TimedRotatingFileHandler


def setup_logger(log_file="logs/chatlog"):
    logger = logging.getLogger("my_logger")
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=15, utc=True)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
