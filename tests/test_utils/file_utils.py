from typing import List

import glob


def get_all_files_in_directory_recursively(directory: str) -> List[str]:
    """Returns a list of all file paths in a directory recursively

    Args:
        directory (str): Directory to get all file paths

    Returns:
        List[str]: Returns a list of file paths
    """
    return glob.glob(directory + "/**/*", recursive=True)
