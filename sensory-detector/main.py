from modules.CustomLogger import CustomLogger


def main() -> None:
    logger = CustomLogger(__name__).get_logger()
    logger.info("Starting up Rescate-tance sensory detector")

    logger.info("Shutting down Rescate-tance sensory detector")


main()
