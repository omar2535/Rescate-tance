# Logger

import logging
import os
from constants import DEFAULT_LOG_FILE

DEFAULT_LOGGING_LEVEL = logging.INFO
DEFAULT_LOGGING_FORMAT = "%(asctime)s : %(levelname)s : %(name)s : %(message)s"


class CustomLogger:
    def __init__(self, name: str, file_name=DEFAULT_LOG_FILE) -> logging:
        self.file_name = file_name
        # Set up logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(DEFAULT_LOGGING_LEVEL)
        file_handler = logging.FileHandler(file_name)
        formatter = logging.Formatter(DEFAULT_LOGGING_FORMAT)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger
