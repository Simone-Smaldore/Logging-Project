import logging.config
import json
import pathlib

logger = logging.getLogger("my_app")


def setup_logging(file_path: str) -> None:
    """
    Setup the application logger passing the file path of a json setup file

    Args :
        file_path (str): the relative file path to the logger json file
    """
    config_file = pathlib.Path(file_path)
    with open(config_file) as file_conf:
        logging_config = json.load(file_conf)
    logging.config.dictConfig(config=logging_config)


def main():
    file_path = "config-logger.json"
    setup_logging(file_path=file_path)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")


if __name__ == "__main__":
    main()
