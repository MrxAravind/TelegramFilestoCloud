import logging
from logging.handlers import RotatingFileHandler
from config import *



# Messages

SOURCE = "\n\nSource: [TelegramFilestoCloud](https://github.com/MrxAravind/TelegramFilestoCloud)"
START = "\n\n**~~This bot uploads telegram files to a third-party server~~**.\n\nAdmin: __[MrSpidy](" \
        "tg://user?id=429320566)__"
ERROR = "something is went wrong\n{error}"
HELP = "\n\nUsage: **Send any file or bot. Then select the third-party Cloud you want to upload to.**"


# LOGGER

LOGGER_FILE_NAME = "filetocloud_log.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOGGER_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ])
logging.getLogger('pyrogram').setLevel(logging.WARNING)


def LOGGER(log: str) -> logging.Logger:
    """Logger function"""
    return logging.getLogger(log)
