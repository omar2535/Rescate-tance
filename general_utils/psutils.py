import psutil


def getPidOfProcessByName(processName):
    """
    Check if there is any running process that contains the given name processName.
    https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
    """
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None
