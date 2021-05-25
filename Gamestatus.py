from enum import Enum


class GameStatus(Enum):
    WIN = 1
    LOSE = 2
    IN_PROGRESS = 3
    NOT_STARTED = 4