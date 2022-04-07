import os
import psutil
from general_utils.iotop import get_iotop_processes


def terminate():
    get_iotop_processes()
