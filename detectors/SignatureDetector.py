from detectors.Detector import Detector

import requests
import subprocess

# This script first interacts with terminal with "ps -a" to get all processes PIDs
# Then use PIDs to get the files and corresponding sha256
# fill VirusTotal API with sha256 and get data of the file from its malware database
# url for VirusTotal API: https://developers.virustotal.com/reference/getting-started


class SignatureDetector(Detector):
    def __init__(self):
        pass

    def run(self):
        # get all running processes PID
        all_process = subprocess.check_output(["ps", "-a"])
        string = str(all_process)
        process_list = string.split("\\n")
        for m in range(1, len(process_list)):
            process = process_list[m]
            procStr = process.strip()
            j = 0
            for i in range(0, len(procStr)):
                if procStr[i] == " ":
                    j = i
                    break
            pid_str = procStr[0:j]
            if len(pid_str) == 0 or pid_str[0] > "9" or pid_str[0] < "0":
                continue

            # get path of file using PID
            path_of_file = "/proc/" + pid_str + "/exe"
            path_str = subprocess.check_output(["readlink", "-f", path_of_file])

            str_path = path_str.decode("utf-8")
            str_of_path = str_path[0 : len(str_path) - 1]

            # get sha256 of file using path of file
            str_sha256 = subprocess.check_output(["shasum", "-a", "256", str_of_path])

            sha256_str = str_sha256.decode("utf-8")

            shaEnd = 0
            for index in range(0, len(sha256_str)):
                if sha256_str[index] == " ":
                    shaEnd = index
                    break
            sha256 = sha256_str[0:shaEnd]

            # API
            url = "https://www.virustotal.com/api/v3/files/" + sha256
            headers = {
                "Accept": "application/json",
                "x-apikey": "5253c6e4b86d0aedc4dbe53ce694e9b0c30a3653db02681dea220bc413f6c5c5",
            }
            response = requests.request("GET", url, headers=headers)

            # get response in form of json
            r = response.json()

            # time_mal: malicious times in last analysis stats
            # time_sus: suspicious times in last analysis stats
            time_mal = r["data"]["attributes"]["last_analysis_stats"]["malicious"]
            time_sus = r["data"]["attributes"]["last_analysis_stats"]["suspicious"]
            if time_mal != 0:
                print("Process with PID " + pid_str + " is malicious")
            elif time_sus != 0:
                print("Process with PID " + pid_str + " is suspicious")
            else:
                print("Process with PID " + pid_str + " is safe")
