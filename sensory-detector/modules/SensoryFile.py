# Sensory file class

from constants import SENSORY_FILE_CONTENTS
from CustomLogger import CustomLogger
import os


class SensoryFile:
    def __init__(self, file_path):
        self.logger = CustomLogger(__name__).get_logger()
        self.file_path = file_path

    def check(self):
        # TODO: Check if the file was changed / encrypted
        pass

    def create(self):
        try:
            f = open(f"{self.file_path}", "x")
            f.write(SENSORY_FILE_CONTENTS)
            f.close()
        except FileExistsError:
            self.logger.warning(f"Creating file '{self.file_path}' already exists")

    def delete(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        else:
            self.logger.warning(f"Delete file '{self.file_path}' doesn't exist!")
