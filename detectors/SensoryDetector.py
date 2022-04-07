from general_utils.CustomLogger import CustomLogger
from general_utils.log_utils import do_rollover
from sensory_detector.modules.SensoryFile import SensoryFile
from constants import CONFIG_FILE_PATH, DEFAULT_LOG_FILE, MAX_LOG_FILES_TO_KEEP
from sensory_detector.utils.file_utils import get_list_of_sensor_paths
from sensory_detector.utils.RepeatedTimer import RepeatedTimer
from detectors.Detector import Detector

from typing import List
import yaml
import time
import threading
import signal
import logging


class SensoryDetector(Detector):
    def __init__(self):
        """Initialize sensor files, timers, and loggers"""
        self.sensor_files: List[SensoryFile] = []
        self.repeated_timers: List[RepeatedTimer] = []
        self.logger: logging.Logger = None

        """Setup logger"""
        do_rollover(MAX_LOG_FILES_TO_KEEP, DEFAULT_LOG_FILE)
        self.custom_logger = CustomLogger(__name__)
        self.logger = self.custom_logger.get_logger()

        def shutdown(signum, frame) -> None:
            """Deletes sensor files and stops timers"""
            for sensor_file in self.sensor_files:
                sensor_file.delete()
            for rt in self.repeated_timers:
                rt.stop()

            print("\r(-) Stopping rescate-tance sensory file detector!")
            self.logger.info("Shutting down Rescate-tance sensory detector")
            exit(1)

        """Setup signal"""
        signal.signal(signal.SIGINT, shutdown)

    def run(self):
        """Creates sensor files and registers timers to check sensor files"""

        self.logger.info("Starting up Rescate-tance sensory detector")

        """ Read and create file paths """
        config_file_stream = open(CONFIG_FILE_PATH, "r")
        config = yaml.safe_load(config_file_stream)
        dir_paths = config["directories_to_check"]
        file_paths = get_list_of_sensor_paths(dir_paths)

        """ Create sensor files """
        for file_path in file_paths:
            sensor_file = SensoryFile(file_path)
            sensor_file.create()
            self.sensor_files.append(sensor_file)

        """ Register timers to check sensor files """
        for sensor_file in self.sensor_files:
            check_frequency = config["frequency_to_check"]
            rt = RepeatedTimer(check_frequency, sensor_file.check)
            self.repeated_timers.append(rt)

        """ Infinite loop """
        while True:
            time.sleep(1000)
