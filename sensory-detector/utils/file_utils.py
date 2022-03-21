# File utils
def get_file_name_from_file_path(file_path: str) -> str:
    """Gets the file name from a file path

    Args:
        file_path (str): File path

    Returns:
        str: File name
    """
    return file_path.split("/")[-1]
