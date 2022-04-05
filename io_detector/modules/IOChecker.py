import shlex
import subprocess
from getpass import getpass
from typing import List
import pandas as pd


class IOChecker:
    def __init__(self, threshold, sudo_pass):
        self.threshold = threshold
        self.command = shlex.split("sudo -S iotop -obPk -n 1")
        self.sudo_pass = sudo_pass

    def check(self) -> List:
        # print('Suspicious Processes:')
        
        stats = subprocess.run(self.command, stdout=subprocess.PIPE, input=self.sudo_pass, encoding='ascii')

        # split output
        lines = stats.stdout.split('\n')
        for i in range(len(lines)):
            lines[i] = lines[i].split()

        # [['Total', 'DISK', 'READ:', '0.00', 'K/s', '|', 'Total', 'DISK', 'WRITE:', '25278.02', 'K/s'],
        # ['Current', 'DISK', 'READ:', '0.00', 'K/s', '|', 'Current', 'DISK', 'WRITE:', '0.00', 'K/s'],
        # ['PID', 'PRIO', 'USER', 'DISK', 'READ', 'DISK', 'WRITE', 'SWAPIN', 'IO', 'COMMAND'],
        # ['4725', 'be/4', 'user', '0.00', 'K/s', '25278.02', 'K/s', '0.00', '%', '0.01', '%', 'firefox', '-new-window'],
        # []]

        # process data (all in K/s)
        total_disk_read = float(lines[0][3])
        total_disk_write = float(lines[0][9])
        current_disk_read = float(lines[1][3])
        current_disk_write = float(lines[1][9])
        suspicious_processes = []
        if len(lines[3]) > 0:
            for i in range(3, len(lines) - 1):
                process = {'PID': lines[i][0], 'PRIO': lines[i][1], 'USER': lines[i][2], 'DISK_READ': float(lines[i][3]), 'DISK_WRITE': float(
                    lines[i][5]), 'SWAPIN%': float(lines[i][7]), 'IO%': float(lines[i][9]), 'COMMAND': ' '.join(lines[i][11:])}
                # TODO: add more filters
                if process['DISK_WRITE'] > self.threshold['DISK_WRITE']:
                    suspicious_processes.append(process)
        # print(pd.DataFrame(suspicious_processes), flush=True)
        return suspicious_processes
        
