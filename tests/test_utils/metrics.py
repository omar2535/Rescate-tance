from typing import Dict, List


def compute_ransomware_encryption_metrics(before_files: List[str], after_files: List[str]) -> Dict:
    """Computes metrics based on how many files were renamed before and after

    Args:
        before_files (List[str]): List of file paths before ransomware encryption
        after_files (List[str]): List of file paths after ransomware encryption

    Returns:
        Dict: Metrics as a dictionary
    """
    original_num_files = len(before_files)
    before_files_not_in_after_files = list(set(before_files) - set(after_files))
    num_files_encrypted = len(before_files_not_in_after_files)
    num_files_not_encrypted = original_num_files - num_files_encrypted
    percentage_of_files_encrypted = round(num_files_encrypted / original_num_files * 100, 2)

    return {
        "percentage_encrypted": percentage_of_files_encrypted,
        "num_files_encrypted": num_files_encrypted,
        "num_files_not_encrypted": num_files_not_encrypted,
        "original_num_files": original_num_files,
    }
