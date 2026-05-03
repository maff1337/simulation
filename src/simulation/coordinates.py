from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    row: int
    column: int

    def __post_init__(self) -> None:
        if self.row < 0 or self.column < 0:
            raise ValueError(f'Coordinates cannot be negative: {self}')
