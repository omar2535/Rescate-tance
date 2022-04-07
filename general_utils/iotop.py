import shlex
import subprocess


def get_iotop_processes():
    command = shlex.split("sudo -S iotop -obPk -n 5")
    stats = subprocess.run(command, stdout=subprocess.PIPE, encoding="utf-8")
    lines = stats.stdout.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].split()
    breakpoint()
    return lines
