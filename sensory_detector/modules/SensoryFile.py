# Sensory file class

from constants import SENSORY_FILE_CONTENTS
from general_utils.CustomLogger import CustomLogger

import psutil
import os


class SensoryFile:
    def __init__(self, file_path, logger: CustomLogger):
        self.logger = logger
        self.file_path = file_path

    def check(self) -> bool:
        """Check if the contents of sensor file is same. Throws exception if file was changed

        Returns:
            bool: _description_
        """
        try:
            if not os.path.exists(self.file_path):
                raise Exception("File was deleted or changed!")

            with open(f"{self.file_path}", "r") as f:
                content = f.read()
                f.close()
            self.logger.info(f"Checked {self.file_path}")
            if content == SENSORY_FILE_CONTENTS:
                return
            else:
                raise Exception("File was changed!")
        except Exception:
            # TODO: Change to general purpose handler (right now, only specific to RAASNET)
            os.system("pkill -9 -f raasnet_payload.py")
            pass

    def create(self):
        """Create sensor file"""
        try:
            os.umask(0)
            with open(os.open(f"{self.file_path}", os.O_CREAT | os.O_WRONLY, 0o777), "x") as f:
                f.write(SENSORY_FILE_CONTENTS)
                f.close()
            self.logger.info(f"Sensory file {self.file_path} created")
        except FileExistsError:
            self.logger.warning(f"Creating file '{self.file_path}' already exists")
            pass

    def delete(self):
        """Delete sensor file"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            self.logger.info(f"Sensory file {self.file_path} deleted")
        else:
            self.logger.warning(f"Delete file '{self.file_path}' doesn't exist!")
            pass
