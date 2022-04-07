from .SensoryDetector import SensoryDetector
from .IODetector import IODetector
from .SignatureDetector import SignatureDetector

available_detectors = {
    "SensoryDetector": SensoryDetector,
    "IODetector": IODetector,
    "SignatureDetector": SignatureDetector,
}
