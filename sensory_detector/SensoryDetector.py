from general_utils.CustomLogger import CustomLogger
from general_utils.log_utils import do_rollover
from modules.SensoryFile import SensoryFile
from constants import CONFIG_FILE_PATH, DEFAULT_LOG_FILE, MAX_LOG_FILES_TO_KEEP
from utils.file_utils import get_list_of_sensor_paths
from utils.RepeatedTimer import RepeatedTimer

from typing import List
import yaml
import time
import threading
import signal
import logging

class SensoryDetector(Detector):
    def __init__(self):
        """Setup logger"""
        do_rollover(MAX_LOG_FILES_TO_KEEP, DEFAULT_LOG_FILE)
        custom_logger = CustomLogger(__name__)
        logger = custom_logger.get_logger()
        
        """Setup signal"""
        signal.signal(signal.SIGINT, shutdown)
    
    def run(self):
        pass
    
    
    def shutdown(self):
        pass
