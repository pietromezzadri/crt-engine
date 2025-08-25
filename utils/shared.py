from enum import Enum


class GameState(Enum):
    LOADING = "LOADING"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    TITLE_SCREEN = "TITLE_SCREEN"
    END = "END"
