from simulation.actions.action import Action
from simulation.entities import Creature
from simulation.path_finder import PathFinder
from simulation.world import World


class MakeMoveAction(Action):
    def __init__(self, path_finder: PathFinder) -> None:
        self._path_finder = path_finder

    def perform(self, world: World) -> None:
        for entity in world.get_entities():
            if not isinstance(entity, Creature) or entity.hp <= 0:
                continue

            while entity.action_points:

                coords = world.get_coordinates(entity)

                if not coords:
                    raise ValueError()

                path = self._path_finder.find(coords, world)

                if not len(path):
                    neighbors = world.get_neighbors(coords)
                    target_found = False

                    for neighbor in neighbors:
                        target = world.get_entity(neighbor)

                        if target and isinstance(target, entity.target):
                            entity.bite(target)
                            target_found = True

                    if not target_found:
                        break
                else:
                    moves: int
                    if len(path) >= entity.action_points:
                        moves = entity.action_points
                    else:
                        moves = len(path)

                    world.update_coordinates(entity, path[moves-1])
                    entity.action_points -= moves
