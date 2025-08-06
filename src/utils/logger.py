import logging
import sys
from typing import Optional


def get_logger(name: str, level: str = "INFO", stream: Optional[object] = None) -> logging.Logger:
    """Return a configured :class:`logging.Logger` instance.

    The function ensures that loggers are configured in a consistent way across
    the project. Handlers are only added once which makes the function safe to
    call multiple times.  By default logs are written to ``stdout``.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(stream or sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
    logger.setLevel(level.upper())
    return logger
