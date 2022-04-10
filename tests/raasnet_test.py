import os
import sys
import time
import pathlib
import shutil
import itertools
import subprocess
import randomfiletree

from file_generator.generate_random_file_tree import generate_random_files

FILE_PATH = os.path.abspath(os.path.dirname(__file__))
DETECTOR_TO_TEST = "SensoryDetector"


def test():
    """
    This script will be responsible to benchmarking our program (Rescate-tance) detector VS RAASNET

    The script will perform the following steps:

    0. Cleanup the test_folder
    1. Install raasnet dependencies
    2. Create a bunch of dummy folders and dummy files
    3. Run the detector (`python3 main.py -d <detector>`)
    4. Run RAASNET (`python3 tests/ransomware/raasnet_payload.py`)
    5. If the detector raises an exception, stop RAASnet and time how long it took and what percentage of files were encrypted
    """

    """0. Clean up test folder"""
    try:
        shutil.rmtree(f"{FILE_PATH}/test_folder")
    except OSError:
        print("Test folder doesn't exist, skipping clean up of test folder")

    """1. Install dependencies for raasnet"""
    try:
        print("(+) Installing dependencies")
        os.system(
            "sudo apt install iotop python3-pip python3-tk python3-pil python3-pil.imagetk libgeoip1 libgeoip-dev geoip-bin > /dev/null 2>&1"
        )
    except Exception:
        print("(+) Couldn't install linux apt packages")

    try:
        subprocess.check_output(["pip3", "install", "-r", "requirements.txt"])
    except Exception:
        print("(+) Can't install dependencies")

    """2. Create a bunch of dummy folders and dummy files"""
    print("(+) Creating dummy files")
    randomfiletree.core.iterative_gaussian_tree(
        f"{FILE_PATH}/test_folder", nfiles=10, nfolders=5, maxdepth=3, repeat=3, payload=generate_random_files
    )

    """3. Run the detector"""
    os.chdir(f"{FILE_PATH}/../")
    detector_proc = subprocess.Popen(f"sudo python3 main.py -d {DETECTOR_TO_TEST}", shell=False)
    # os.system(f"sudo python3 main.py -d {DETECTOR_TO_TEST}")

    """4. Run the ransomware"""
    raasnet_proc = subprocess.Popen(f"sudo python3 tests/ransomware/raasnet_payload.py")
    
    # TODO: Kill detector & ransomware only so we can keep metrics in this script
    # Generate a file tree of previous, then for each file in previous file tree, check percentage of encryption