from random import randrange
from typing import Optional, Sequence

from simulation.entities import Entity
from simulation.coordinates import Coordinates


class World:
    def __init__(self, rows: int, columns: int, minsize: int) -> None:
        self._rows = rows
        self._columns = columns

        self._entities: dict[Entity, Coordinates] = {}

        if self.size() < minsize:
            raise

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def columns(self) -> int:
        return self._columns

    def size(self) -> int:
        return self._rows * self._columns

    def get_entities(self) -> Sequence[Entity]:
        return list(self._entities.keys())

    def _get_random_coordinates(self) -> Coordinates:
        row = randrange(self._rows)
        column = randrange(self._columns)

        return Coordinates(row, column)

    def get_empty_coordinates(self) -> Coordinates:
        while True:
            coords = self._get_random_coordinates()

            if coords not in self._entities.values():
                return coords

    def add_entity(self, entity: Entity) -> None:
        if self.is_full():
            return

        coords = self.get_empty_coordinates()

        self._entities[entity] = coords

    def delete_entity(self, entity: Entity) -> None:
        if entity in self._entities.keys():
            del self._entities[entity]

    def get_entity(self, coordinates: Coordinates) -> Optional[Entity]:
        for entity, coords in self._entities.items():
            if coords == coordinates:
                return entity

        return None

    def get_coordinates(self, entity: Entity) -> Optional[Coordinates]:
        return self._entities.get(entity)

    def get_neighbors(self, coords: Coordinates) -> Sequence[Coordinates]:
        shifts = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        shifted = [
            Coordinates(
                coords.row + shift[0],
                coords.column + shift[1]
            )
            for shift in shifts
        ]

        return [
            coords for coords in shifted
            if 0 <= coords.row < self.rows and 0 <= coords.column < self.columns
        ]

    def is_full(self) -> bool:
        return len(self._entities) == self.size()

    def update_coordinates(self, entity: Entity, coords: Coordinates) -> None:
        self._entities[entity] = coords
