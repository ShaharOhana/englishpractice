from dataclasses import dataclass


@dataclass
class GameMode:
    WITH_HINTS: int = 1
    WITHOUT_HINTS: int = 2
