"""
    Game Actions Keys
"""
from pygame import constants
from enum import Enum


class Menu(Enum):
    SELECT = constants.K_RETURN
    START = constants.K_p
    PAUSE = constants.K_ESCAPE
<<<<<<< Updated upstream
    SELECT = constants.K_RETURN
    DOWN = constants.K_DOWN
    UP = constants.K_UP
    RIGHT = constants.K_RIGHT
    LEFT = constants.K_LEFT


class MainGameAction(Enum):
    PAUSE = constants.K_ESCAPE
    DOWN = constants.K_DOWN
    UP = constants.K_UP
    RIGHT = constants.K_RIGHT
    LEFT = constants.K_LEFT
    ZOOM_IN = constants.K_z
    ZOOM_OUT = constants.K_x


class CameraAction(Enum):
    DOWN = constants.K_s
    UP = constants.K_w
    RIGHT = constants.K_d
    LEFT = constants.K_a
    FIND = constants.K_f
=======
    DOWN = [constants.K_DOWN, constants.K_s]
    UP = [constants.K_UP, constants.K_w]
    RIGHT = [constants.K_RIGHT, constants.K_d]
    LEFT = [constants.K_LEFT, constants.K_a]
>>>>>>> Stashed changes


class MainGame(Enum):
    PAUSE = constants.K_ESCAPE
    DOWN = [constants.K_DOWN, constants.K_s]
    UP = [constants.K_UP, constants.K_w]
    RIGHT = [constants.K_RIGHT, constants.K_d]
    LEFT = [constants.K_LEFT, constants.K_a]


class Cutscene(Enum):
    SKIP = constants.K_x


class Entity(Enum):
    RUN = constants.K_LSHIFT
