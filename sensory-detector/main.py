from modules.CustomLogger import CustomLogger
from modules.SensoryFile import SensoryFile
from constants import CONFIG_FILE_PATH, DEFAULT_LOG_FILE, MAX_LOG_FILES_TO_KEEP
from utils.file_utils import get_list_of_sensor_paths
from utils.RepeatedTimer import RepeatedTimer
from utils.log_utils import do_rollover

from typing import List
import yaml
import time
import threading
import signal
import logging

"""Global variable"""
sensor_files: List[SensoryFile] = []
repeated_timers: List[RepeatedTimer] = []
logger: logging.Logger = None


def main() -> None:
    startup()
    while True:
        time.sleep(1000)


def startup():
    """Creates sensor files and registers timers to check sensor files"""

    logger.info("Starting up Rescate-tance sensory detector")

    # Read and create file paths
    config_file_stream = open(CONFIG_FILE_PATH, "r")
    config = yaml.safe_load(config_file_stream)
    dir_paths = config["directories_to_check"]
    file_paths = get_list_of_sensor_paths(dir_paths)

    # Create sensor files
    for file_path in file_paths:
        sensor_file = SensoryFile(file_path)
        sensor_file.create()
        sensor_files.append(sensor_file)

    # Register timers to check sensor files
    for sensor_file in sensor_files:
        check_frequency = config["frequency_to_check"]
        rt = RepeatedTimer(check_frequency, sensor_file.check)
        repeated_timers.append(rt)


def shutdown(signum, frame) -> None:
    """Deletes sensor files and stops timers"""
    for sensor_file in sensor_files:
        sensor_file.delete()
    for rt in repeated_timers:
        rt.stop()

    print("\r(-) Stopping rescate-tance sensory file detector!")
    logger.info("Shutting down Rescate-tance sensory detector")
    exit(1)


"""Register sigint handlers"""
signal.signal(signal.SIGINT, shutdown)

if __name__ == "__main__":
    print("(+) Starting Rescate-tance sensory file detector!")

    """Setup logger"""
    do_rollover(MAX_LOG_FILES_TO_KEEP, DEFAULT_LOG_FILE)
    custom_logger = CustomLogger(__name__)
    logger = custom_logger.get_logger()

    """Call main"""
    main()
