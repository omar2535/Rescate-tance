# Constants
import pathlib

# Program specific constants
SENSORY_FILE_CONTENTS = "rescate-tance"
DESCRIPTION = "A collection of proof-of-concept ransomware detectors"

# General constants
DEFAULT_LOG_FILE = str(pathlib.Path(__file__).parent.resolve()) + "/logs/main.log"
DEFAULT_SENSOR_FILE_NAME = ".rcsensor.txt"

# Configuration files
CONFIG_FILE_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/config.yml"

# Logging constants
MAX_LOG_FILES_TO_KEEP = 10
