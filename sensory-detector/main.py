from modules.CustomLogger import CustomLogger
from modules.SensoryFile import SensoryFile


def main() -> None:
    logger = CustomLogger(__name__).get_logger()
    logger.info("Starting up Rescate-tance sensory detector")

    sf = SensoryFile("./lol.txt")
    sf.create()
    breakpoint()
    sf.check()
    sf.delete()

    logger.info("Shutting down Rescate-tance sensory detector")


main()
