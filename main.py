import argparse
from detectors.SensoryDetector import SensoryDetector
from constants import DESCRIPTION
from detectors import detectors
from general_utils.main_utils import get_list_of_detectors

'''Argument parser'''
parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('-d', type=str, help=f"one of {get_list_of_detectors()}")

detector = SensoryDetector()
args = parser.parse_args()
breakpoint()

print("lol")

# detector.run()
