import os
import logging

if not os.path.exists("logs"):
    os.mkdir("logs")
logging.basicConfig(filename="logs/console.log", filemode="a", encoding="utf-8", level=logging.INFO)


def log(entry):
    """
    Arguments:
        entry: log entry
    Returns:
        None
    """
    logging.info(entry)
