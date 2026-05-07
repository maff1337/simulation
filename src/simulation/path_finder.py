from collections import deque
from abc import abstractmethod
from typing import Protocol, Sequence

from simulation.world import World
from simulation.coordinates import Coordinates
from simulation.entities import Creature, Resource


class PathFinder(Protocol):
    @abstractmethod
    def find(self, start: Coordinates, world: World) -> Sequence[Coordinates]:
        ...


class Bfs(PathFinder):
    def find(self, start: Coordinates, world: World) -> Sequence[Coordinates]:
        base_entity = world.get_entity(start)

        if base_entity is None:
            raise ValueError()

        target_type = base_entity.target

        visited = set([start])
        queue = deque([start])

        came_from = {}

        while queue:
            current = queue.popleft()

            for neighbor in world.get_neighbors(current):
                if neighbor in visited:
                    continue

                entity = world.get_entity(neighbor)
                if entity is None or \
                        (isinstance(entity, (Creature, Resource)) and entity.hp <= 0):
                    queue.append(neighbor)
                    visited.add(neighbor)

                came_from[neighbor] = current

                if isinstance(entity, target_type):
                    return restore_path(start, neighbor, came_from)

        return []


def restore_path(start: Coordinates, end: Coordinates, path: dict[Coordinates, Coordinates]) -> Sequence[Coordinates]:
    reversed_path = []
    came_from = path[end]

    while came_from != start:
        reversed_path.append(came_from)

        came_from = path[came_from]

    return list(reversed(reversed_path))
