import os
import sys
import time
import pathlib
import itertools
import subprocess
import randomfiletree

from file_generator.generate_random_file_tree import generate_random_files

FILE_PATH = os.path.abspath(os.path.dirname(__file__))


def test():
    """
    This script will be responsible to benchmarking our program (Rescate-tance) detector VS RAASNET

    The script will perform the following steps:

    1. Install raasnet dependencies
    2. Create a bunch of dummy folders and dummy files
    3. Run the detector (`python3 main.py -d <detector>`)
    4. Run RAASNET (`python3 tests/ransomware/raasnet_payload.py`)
    5. If the detector raises an exception, stop RAASnet and time how long it took and what percentage of files were encrypted
    """

    """1. Install dependencies for raasnet"""
    try:
        os.system(
            "sudo apt install python3-pip python3-tk python3-pil python3-pil.imagetk libgeoip1 libgeoip-dev geoip-bin"
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
        f"{FILE_PATH}/test_folder", nfiles=2, nfolders=2, maxdepth=2, repeat=2, payload=generate_random_files
    )
