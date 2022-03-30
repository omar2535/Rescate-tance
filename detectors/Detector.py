from general_utils.CustomLogger import CustomLogger
from general_utils.log_utils import do_rollover

# General detector class
class Detector:
    def __init__(self):
        pass

    def run(self):
        raise Exception("Overwrite me!")

    def __str__(self):
        """For print override
        """
        return self.__class__.__name__

    def __repr__(self):
        """For interactive prompt override
        """
        return self
