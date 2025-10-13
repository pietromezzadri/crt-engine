"""
    Game Actions Keys
"""
from pygame import constants
from enum import Enum


class MenuAction(Enum):
    START = constants.K_p
    PAUSE = constants.K_ESCAPE


class MainGameAction(Enum):
    PAUSE = constants.K_ESCAPE
    DOWN = [constants.K_DOWN, constants.K_s]
    UP = [constants.K_UP, constants.K_w]
    RIGHT = [constants.K_RIGHT, constants.K_d]
    LEFT = [constants.K_LEFT, constants.K_a]


class CutsceneAction(Enum):
    SKIP = constants.K_x


class EntityAction(Enum):
    RUN = constants.K_LSHIFT
