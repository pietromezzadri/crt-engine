
"""
    PRESETS for unix terminal
"""
import logging


GREY_BG = "\x1b[30;47m"
BLACK_BG = "\x1b[1;40m"
RED_BG = "\x1b[1;41m"
BLUE_BG = "\x1b[1;44m"
GREEN_BG = "\x1b[1;42m"
MAGENTA_BG = "\x1b[1;45m"
CYAN_BG = "\x1b[30;46m"
YELLOW_BG = "\x1b[30;43m"
WHITE = "\x1b[1m"
GREY = "\x1b[37m"
BLACK = "\x1b[30m"
RED = "\x1b[31m"
BLUE = "\x1b[34m"
GREEN = "\x1b[32m"
MAGENTA = "\x1b[35m"
CYAN = "\x1b[36m"
YELLOW = "\x1b[33m"
RESET = "\x1b[0m"


class Logger:
    """
        Class Responsible for Logging
    """

    def __init__(self, name):
        self.name = name

    def debug(self, msg):
        """
            Debug logger
        """
        logging.root.handlers = []
        logging.basicConfig(
            level=logging.DEBUG,
            format=f"{MAGENTA}{self.name:<15}{RESET} {BLUE_BG}[%(levelname)s]{RESET} \
                {'':<3} {YELLOW}%(message)s{RESET} %(asctime)s",
            handlers=[
                logging.FileHandler("logs/debug.log"),
                logging.StreamHandler()
            ]
        )
        logging.debug(msg)

    def info(self, msg):
        """
            Info logger
        """
        logging.root.handlers = []
        logging.basicConfig(
            level=logging.INFO,
            format=f"{MAGENTA}{self.name:<15}{RESET} {GREY_BG}[%(levelname)s]{RESET} \
                {'':<3} {YELLOW}%(message)s{RESET} %(asctime)s",
            handlers=[
                logging.FileHandler("logs/debug.log"),
                logging.StreamHandler()
            ]
        )
        logging.info(msg)

    def warning(self, msg):
        """
            Warning logger
        """
        logging.root.handlers = []
        logging.basicConfig(
            level=logging.WARNING,
            format=f"{MAGENTA}{self.name:<15}{RESET} {YELLOW_BG}[%(levelname)s]{RESET} \
                {'':<3} {YELLOW}%(message)s{RESET} %(asctime)s",
            handlers=[
                logging.FileHandler("logs/debug.log"),
                logging.StreamHandler()
            ]
        )
        logging.warning(msg)

    def error(self, msg):
        """
            ERROR logger
        """
        logging.root.handlers = []
        logging.basicConfig(
            level=logging.ERROR,
            format=f"{MAGENTA}{self.name:<15}{RESET} {RED_BG}[%(levelname)s]{RESET} \
                {'':<3} {YELLOW}%(message)s{RESET} %(asctime)s",
            handlers=[
                logging.FileHandler("logs/debug.log"),
                logging.StreamHandler()
            ]
        )
        logging.error(msg)
