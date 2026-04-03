from enum import Enum


class GameState(Enum):
    LOADING = "LOADING"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    TITLE_SCREEN = "TITLE_SCREEN"
    SETTINGS = "SETTINGS"
    END = "END"


class EngineState(Enum):
    LOADING = "LOADING"
    RUNNING = "RUNNING"
    END = "END"


class GameMode(Enum):
    DEBUG = "DEBUG"
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"
<<<<<<< Updated upstream
=======


class ButtonState(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class GameEvents(Enum):
    START_GAME = "START GAME"
    PAUSE_GAME = "PAUSE GAME"
    END_GAME = "END GAME"
    RESTART_GAME = "RESTART GAME"
    START_EVENT = "START EVENT"
    PAUSE_EVENT = "PAUSE EVENT"
    END_EVENT = "END EVENT"
    RESTART_EVENT = "RESTART EVENT"


class ConfigMode(Enum):
    GRAPHICS_CONFIG = "GRAPHICS CONFIGURATION"
    CHANGE_RESOLUTION = "CHANGE RESOLUTION"
    SELECT_RESOLUTION = "SELECT RESOLUTION"


class MenuType(Enum):
    STANDARD_H = "STANDARD HORIZONTAL"
    STANDARD_V = "STANDARD VERTICAL"


class UI(Enum):
    MAIN_MENU = "MAIN MENU"
    PAUSE_MENU = "PAUSE MENU"
    CONFIG_MENU = "CONFIG MENU"
>>>>>>> Stashed changes
