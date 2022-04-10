import os
import psutil
from general_utils.iotop import get_iotop_processes


def post_detection_handler():
    """Post detection handler. Put kill command here or whatever the process is when ransomware is detected"""
    # TODO: Change this to something general, likely able to use iotop to get
    # TODO: highest IO process' PID then kill
    os.system("pkill -9 -f raasnet_payload.py")
