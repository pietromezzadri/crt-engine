from enum import Enum


class GameState(Enum):
    LOADING = "LOADING"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    TITLE_SCREEN = "TITLE_SCREEN"
    END = "END"

class EngineState(Enum):
    LOADING = "LOADING"
    RUNNING = "RUNNING"
    END = "END"

class GameMode(Enum):
    DEBUG = "DEBUG"
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"