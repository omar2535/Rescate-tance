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


def cleanup_test_folder():
    try:
        shutil.rmtree(f"{FILE_PATH}/test_folder")
    except OSError:
        print("Test folder doesn't exist, skipping clean up of test folder")


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
    cleanup_test_folder()

    """1. Install dependencies for raasnet"""
    try:
        print("(test) Installing dependencies")
        os.system(
            "sudo apt install iotop python3-pip python3-tk python3-pil python3-pil.imagetk libgeoip1 libgeoip-dev geoip-bin > /dev/null 2>&1"
        )
    except Exception:
        print("(test) Couldn't install linux apt packages")

    try:
        subprocess.check_output(["pip3", "install", "-r", "requirements.txt"])
    except Exception:
        print("(test) Can't install dependencies")

    """2. Create a bunch of dummy folders and dummy files"""
    print("(test) Creating dummy files")
    randomfiletree.core.iterative_gaussian_tree(
        f"{FILE_PATH}/test_folder", nfiles=10, nfolders=5, maxdepth=3, repeat=3, payload=generate_random_files
    )

    """3. Run the detector"""
    os.chdir(f"{FILE_PATH}/../")
    detector_proc = subprocess.Popen(["sudo", "python3", "main.py", "-d", DETECTOR_TO_TEST], shell=False)
    # os.system(f"sudo python3 main.py -d {DETECTOR_TO_TEST}")

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

    """"6. Cleanup test folder again"""
    # cleanup_test_folder()

    # find ./tests/test_folder -type f -name "*.docx"

    # TODO: Kill detector & ransomware only so we can keep metrics in this script
    # Generate a file tree of previous, then for each file in previous file tree, check percentage of encryption
