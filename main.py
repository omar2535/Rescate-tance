import os
import sys
import argparse
from typing import List
from detectors.SensoryDetector import SensoryDetector
from constants import DESCRIPTION
from detectors import available_detectors

"""Get list of detectors"""
list_of_detectors: List[str] = list(available_detectors.keys())

"""Argument parser"""
parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument("-d", "--detector", type=str, help=f"one of {list_of_detectors}")
args = parser.parse_args()

"""Run the detector that was specified"""
if args.detector in available_detectors:
    available_detectors[args.detector]().run()
else:
    print("(+) No detector found for: {args.detector}")
