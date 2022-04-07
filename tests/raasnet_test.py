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

    1. Clone the RAASNET repository & install dependencies
    2. Create a bunch of dummy folders and dummy files
    3. Run the detector (`python3 main.py -d <detector>`)
    4. Run RAASNET (`python3 tests/ransomware/raasnet_payload.py`)
    5. If the detector raises an exception, stop RAASnet and time how long it took and what percentage of files were encrypted
    """

    """1. Clone the RAASNET repository & install dependencies"""
    try:
        subprocess.check_output(["git", "clone", "https://github.com/leonv024/RAASNet.git", f"{FILE_PATH}/RAASNet"])
    except Exception:
        print("(+) Couldn't clone the RAASNET repository")

    try:
        os.system(
            "sudo apt install python3-pip python3-tk python3-pil python3-pil.imagetk libgeoip1 libgeoip-dev geoip-bin"
        )
    except Exception:
        print("(+) Couldn't install linux apt packages")

    try:
        subprocess.check_output(["pip3", "install", "-r", f"{FILE_PATH}/RAASNet/requirements.txt"])
    except Exception:
        print("(+) Can't install RAASNet pip dependencies")

    """2. Create a bunch of dummy folders and dummy files"""
    print("(+) Creating dummy files")
    randomfiletree.core.iterative_gaussian_tree(
        f"{FILE_PATH}/test_folder", nfiles=5, nfolders=5, maxdepth=3, repeat=4, payload=generate_random_files
    )
