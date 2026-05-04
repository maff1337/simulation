from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    row: int
    column: int
