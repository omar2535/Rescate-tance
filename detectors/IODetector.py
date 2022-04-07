import imp
from general_utils.CustomLogger import CustomLogger
from detectors.Detector import Detector
from io_detector.modules.IOChecker import IOChecker
from getpass import getpass

from typing import List
import yaml
import time


class IODetector(Detector):
    def __init__(self):
        # TODO Parse threshold and interval
        self.threshold = {"DISK_READ": 0, "DISK_WRITE": 0, "SWAPIN%": 0, "IO%": 0}
        self.interval = 5
        self.sudo_pass = None  # getpass('Password: ')
        self.io_checker = IOChecker(threshold=self.threshold, sudo_pass=self.sudo_pass)

    def run(self):
        while True:
            suspicious_processes = self.io_checker.get_suspicious_processes()
            # TODO log processes
            print(suspicious_processes)
            time.sleep(self.interval)
