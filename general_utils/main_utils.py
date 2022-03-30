from detectors import detectors
from typing import List

def get_list_of_detectors() -> List[str]:
    """Returns the list of detecotrs

    Returns:
        List: Returns list of detectors as a string
    """
    return list(map(lambda detector: detector.__name__, detectors))
