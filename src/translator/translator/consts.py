from dataclasses import dataclass

HINT_CHAR = '?'


@dataclass
class GameMode:
    WITH_HINTS: int = 1
    WITHOUT_HINTS: int = 2

    @classmethod
    def values(cls):
        return [GameMode.WITH_HINTS, GameMode. WITHOUT_HINTS]
