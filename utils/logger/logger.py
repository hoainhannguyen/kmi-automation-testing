import logging

logging.basicConfig(filename="./logs/console.log", filemode="a", encoding="utf-8", level=logging.INFO)

def log(entry):
    """
    Arguments:
        entry: log entry
    Returns:
        None
    """
    logging.info(entry)
