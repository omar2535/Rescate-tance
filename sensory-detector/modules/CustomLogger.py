# Logger

import logging
import os
from constants import DEFAULT_LOG_FILE

MAX_LOG_FILES_TO_KEEP = 10
DEFAULT_LOGGING_LEVEL = logging.INFO
DEFAULT_LOGGING_FORMAT = "%(asctime)s : %(levelname)s : %(name)s : %(message)s"


class CustomLogger:
    def __init__(self, name: str, file_name=DEFAULT_LOG_FILE) -> logging:
        # Do log rotations first
        self.do_rollover(file_name)

        # Set up logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(DEFAULT_LOGGING_LEVEL)
        file_handler = logging.FileHandler(file_name)
        formatter = logging.Formatter(DEFAULT_LOGGING_FORMAT)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

    def do_rollover(self, orig_file_name: str) -> None:
        """Performs log rotations
        main.log -> main-1.log
        main-1.log -> main-2.log
        main-2.log -> main-3.log
        ...
        main-10.log gets deleted

        Args:
            orig_file_name (str): Log file name
        """
        file_extension = orig_file_name.split(".")[-1]
        file_path_without_extension = "".join(orig_file_name.split(".")[0:-1])
        for index in range(MAX_LOG_FILES_TO_KEEP, -1, -1):
            cur_file_name = f"{file_path_without_extension}-{index}.{file_extension}"
            if index == 10 and os.path.isfile(cur_file_name):
                os.remove(cur_file_name)
                continue
            elif index == 0 and os.path.isfile(orig_file_name):
                new_file_name = f"{file_path_without_extension}-{index+1}.{file_extension}"
                os.rename(orig_file_name, new_file_name)
            elif os.path.isfile(cur_file_name):
                new_file_name = f"{file_path_without_extension}-{index+1}.{file_extension}"
                os.rename(cur_file_name, new_file_name)
