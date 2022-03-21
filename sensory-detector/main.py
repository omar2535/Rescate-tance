from modules.CustomLogger import CustomLogger
from modules.SensoryFile import SensoryFile
from constants import CONFIG_FILE_PATH
from utils.file_utils import get_list_of_sensor_paths

from typing import List
import yaml


"""Global variable to hold our sensor file list"""
sensor_files: List[SensoryFile] = []


def main() -> None:
    """Start up logger for main"""
    logger = CustomLogger(__name__).get_logger()
    logger.info("Starting up Rescate-tance sensory detector")

    """Read and create file paths"""
    config_file_stream = open(CONFIG_FILE_PATH, "r")
    config = yaml.safe_load(config_file_stream)
    dir_paths = config["directories_to_check"]
    file_paths = get_list_of_sensor_paths(dir_paths)

    """Create sensor files"""
    for file_path in file_paths:
        sensor_file = SensoryFile(file_path)
        sensor_file.create()
        sensor_files.append(sensor_file)

    # TODO: Make infinite loop to check sensor files,
    # then extend to kill ransomware when change is detected
    """Check sensor files"""
    for sensor_file in sensor_files:
        sensor_file.check()

    # TODO: Make a handler for sigint such that on sigint, the sensor files
    # are deleted automatically
    """Delete sensor files"""
    for sensor_file in sensor_files:
        sensor_file.delete()

    logger.info("Shutting down Rescate-tance sensory detector")


if __name__ == "__main__":
    main()
