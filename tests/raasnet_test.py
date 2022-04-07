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

    1. Clone the RAASNET repository
    2. Create a bunch of dummy folders and dummy files
    3. Configure RAASNET to do ransomware only on the specified dummy folders & files
    4. Run the detector
    5. Run RAASNET
    6. If the detector raises an exception, stop RAASnet and time how long it took and what percentage of files were encrypted
    """

    """1. Clone the RAASNET repository"""
    try:
        subprocess.check_output(["git", "clone", "https://github.com/leonv024/RAASNet.git", f"{FILE_PATH}/RAASNet"])
    except Exception:
        print("(+) Couldn't clone the RAASNET repository")

    """2. Create a bunch of dummy folders and dummy files"""
    randomfiletree.core.iterative_gaussian_tree(
        f"{FILE_PATH}/test_folder", nfiles=5, nfolders=5, maxdepth=3, repeat=4, payload=generate_random_files
    )

    """3. Configure RAASNET to do ransomware only on the specified dummy folders & files"""
