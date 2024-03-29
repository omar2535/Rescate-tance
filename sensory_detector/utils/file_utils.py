import os
from typing import List
from constants import DEFAULT_SENSOR_FILE_NAME


# File utils
def get_file_name_from_file_path(file_path: str) -> str:
    """Gets the file name from a file path

    Args:
        file_path (str): File path

    Returns:
        str: File name
    """
    return file_path.split("/")[-1]


def get_list_of_sensor_paths(dir_paths: List[str]) -> List[str]:
    """Generate a list of file paths as directory + file_name

    Args:
        directories (List[str]): List of directories to have files in

    Returns:
        List[str]: List of file paths
    """
    file_path_list = []
    for directory in dir_paths:
        file_path_list.append(f"{directory.rstrip('//')}/{DEFAULT_SENSOR_FILE_NAME}")
    return file_path_list


def get_list_of_sensor_paths_recursive(dir_paths: List[str]) -> List[str]:
    """Generates list of sensor paths in every folder and subfolder

    Args:
        dir_paths (List[str]): List of directory paths to recursively crawl through

    Returns:
        List[str]: List of sensor file paths
    """
    file_path_list = []
    for directory in dir_paths:
        for sub_dir_obj in os.walk(directory):
            file_path_list.append(f"{sub_dir_obj[0].rstrip('//')}/{DEFAULT_SENSOR_FILE_NAME}")
    return file_path_list
