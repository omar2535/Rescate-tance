import os
import sys
import time
import pprint
import pathlib
import shutil
import itertools
import subprocess
import randomfiletree

from file_generator.generate_random_file_tree import generate_random_files
from .test_utils.file_utils import get_all_files_in_directory_recursively
from .test_utils.metrics import compute_ransomware_encryption_metrics

pp = pprint.PrettyPrinter(indent=2)
FILE_PATH = os.path.abspath(os.path.dirname(__file__))
DETECTOR_TO_TEST = "SensoryDetector"


def cleanup_test_folder():
    try:
        shutil.rmtree(f"{FILE_PATH}/test_folder")
    except OSError:
        print("Test folder doesn't exist, skipping clean up of test folder")


def test():
    """
    This script will be responsible to benchmarking our program (Rescate-tance) detector VS RAASNET
    """

    """0. Clean up test folder"""
    cleanup_test_folder()

    try:
        subprocess.check_output(["pip3", "install", "-r", "requirements.txt"])
    except Exception:
        print("(test) Can't install dependencies")

    """1. Create a bunch of dummy folders and dummy files"""
    print("(test) Creating dummy files")
    randomfiletree.core.iterative_gaussian_tree(
        f"{FILE_PATH}/test_folder", nfiles=10, nfolders=5, maxdepth=3, repeat=3, payload=generate_random_files
    )

    """2. Keep track of original files that were created in test_folder"""
    original_files = get_all_files_in_directory_recursively(f"{FILE_PATH}/test_folder")

    """3. Run the detector"""
    os.chdir(f"{FILE_PATH}/../")
    detector_proc = subprocess.Popen(["sudo", "python3", "main.py", "-d", DETECTOR_TO_TEST], shell=False)

    print("(test) Sleeping a bit for ransomware detector to start up!")
    time.sleep(5)

    """4. Run the ransomware"""
    ransomware_proc = subprocess.Popen(["sudo", "python3", "tests/ransomware/raasnet_payload.py"], shell=False)

    """5. Wait for ransomware to be killed, or after a certain time then just kill everything"""
    print("(test) Sleeping a bit for ransomware to be detected")
    time.sleep(10)
    if ransomware_proc.poll() is None:
        print("(test) Ransomware detector was not able to kill RAASNET :(. Stopping")
    else:
        print("(test) Ransomware detector succesfully stopped RAASNET!")

    detector_proc.kill()
    ransomware_proc.kill()
    os.system("sudo pkill -9 -f SensoryDetector")  # just to make sure the process is killed

    """6: Get files after ransomware hit and check percentage encrypted"""
    after_ransomware_files = get_all_files_in_directory_recursively(f"{FILE_PATH}/test_folder")
    metrics = compute_ransomware_encryption_metrics(original_files, after_ransomware_files)
    pp.pprint(metrics)

    """7. Cleanup test folder again"""
    cleanup_test_folder()
