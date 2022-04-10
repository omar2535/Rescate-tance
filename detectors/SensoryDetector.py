from general_utils.CustomLogger import CustomLogger
from general_utils.log_utils import do_rollover
from sensory_detector.modules.SensoryFile import SensoryFile
from constants import CONFIG_FILE_PATH, DEFAULT_LOG_FILE, MAX_LOG_FILES_TO_KEEP
from sensory_detector.utils.file_utils import get_list_of_sensor_paths, get_list_of_sensor_paths_recursive
from sensory_detector.utils.RepeatedTimer import RepeatedTimer
from detectors.Detector import Detector

from typing import List
from multiprocessing import Pool
import yaml
import time
import threading
import signal
import logging

exit_event = threading.Event()


class SensoryDetector(Detector):
    def __init__(self):
        """Initialize sensor files, timers, and loggers"""
        self.sensor_files: List[SensoryFile] = []
        self.repeated_timers: List[RepeatedTimer] = []
        self.logger: logging.Logger = None

        """Setup logger"""
        do_rollover(MAX_LOG_FILES_TO_KEEP, DEFAULT_LOG_FILE)
        self.logger = CustomLogger(__name__).get_logger()

        def shutdown(signum, frame) -> None:
            """Set exit event for all threads"""
            exit_event.set()

            """Deletes sensor files and stops timers"""
            for rt in self.repeated_timers:
                rt.stop()

            for sensor_file in self.sensor_files:
                sensor_file.delete()

            print("\r(-) Stopping rescate-tance sensory file detector!")
            self.logger.info("Shutting down Rescate-tance sensory detector")
            exit(1)

        """Setup signal"""
        signal.signal(signal.SIGINT, shutdown)

    def run(self):
        """Creates sensor files and registers timers to check sensor files"""

        print("(+) Starting up sensory detector!")
        self.logger.info("Starting up Rescate-tance sensory detector")

        """ Read and create file paths """
        config_file_stream = open(CONFIG_FILE_PATH, "r")
        config = yaml.safe_load(config_file_stream)
        dir_paths = config["directories_to_check"]
        file_paths = get_list_of_sensor_paths_recursive(dir_paths)

        """ Create sensor files """
        for file_path in file_paths:
            sensor_file = SensoryFile(file_path, logger=self.logger)
            sensor_file.create()
            self.sensor_files.append(sensor_file)

        print("(+) Sensory detector up & running!")

        """ Infinite loop, use thread pool to check sensor files """
        while True:
            with Pool(10) as p:
                p.map(SensoryFile.check, self.sensor_files)
            time.sleep(config["frequency_to_check"])
