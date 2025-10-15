from enum import Enum


class MainMenuOptions(Enum):
    START_GAME = "START GAME"
    RESUME = "RESUME"
    SETTINGS = "SETTINGS"
    QUIT = "QUIT"


class ConfigMenuOptions(Enum):
    CHANGE_RES = "CHANGE RESOLUTION"
    BACK = "BACK"
    CONFIRM = "CONFIRM"
