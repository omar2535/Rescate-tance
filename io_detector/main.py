import imp
from typing import List
from modules.IOChecker import IOChecker
from general_utils.log_utils import do_rollover
from general_utils.CustomLogger import CustomLogger
from getpass import getpass
import os
import sys
import time
import pandas as pd

# To fix path to import from upper files
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def main(threshold, interval) -> None:
    sudo_pass = getpass("Password: ")
    io_detector = IOChecker(threshold=threshold, sudo_pass=sudo_pass)
    while True:
        print(io_detector.get_suspicious_processes())
        time.sleep(interval)


if __name__ == "__main__":
    print("(+) Starting Rescate-tance io detector!")
    # TODO: change this part!
    threshold = {"DISK_READ": 0, "DISK_WRITE": 0, "SWAPIN%": 0, "IO%": 0}
    interval = 5

    """Call main"""
    main(threshold, interval)
