# Sensory file class

from constants import SENSORY_FILE_CONTENTS
from general_utils.CustomLogger import CustomLogger
import os


class SensoryFile:
    def __init__(self, file_path):
        self.logger = CustomLogger(__name__).get_logger()
        self.file_path = file_path

    def check(self) -> bool:
        """Check if the contents of sensor file is same. Throws exception if file was changed

        Returns:
            bool: _description_
        """
        f = open(f"{self.file_path}", "r")
        content = f.read()
        f.close()
        self.logger.info(f"Checked {self.file_path}")
        # print(f"check {self.file_path}")
        if content == SENSORY_FILE_CONTENTS:
            return
        else:
            raise Exception("File was changed!")

    def create(self):
        """Create sensor file"""
        try:
            f = open(f"{self.file_path}", "x")
            f.write(SENSORY_FILE_CONTENTS)
            f.close()
            self.logger.info(f"Sensory file {self.file_path} created")
        except FileExistsError:
            self.logger.warning(f"Creating file '{self.file_path}' already exists")

    def delete(self):
        """Delete sensor file"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            self.logger.info(f"Sensory file {self.file_path} deleted")
        else:
            self.logger.warning(f"Delete file '{self.file_path}' doesn't exist!")
