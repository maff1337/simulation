from simulation.world import World
from simulation.entities import Carnivore, Creature, Herbivore
from simulation.actions.action import Action
from simulation.path_finder import PathFinder


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

                path = self._path_finder.find(entity, world)

                if not len(path):
                    neighbors = world.get_neighbors(coords)
                    target_found = False

                    for neighbor in neighbors:
                        target = world.get_entity(neighbor)

                        if isinstance(target, entity.target) and target.hp > 0:  # type: ignore
                            hits = (
                                target.hp // entity.attack +  # type: ignore
                                (target.hp % entity.attack != 0)  # type: ignore
                            )

                            points = min(hits, entity.action_points)

                            while points and target.hp > 0:  # type: ignore
                                entity.bite(target)

                                entity.action_points -= 1

                                points -= 1

                            target_found = True

                    if not target_found:
                        break
                else:
                    moves = min(entity.action_points, len(path))

                    world.update_coordinates(entity, path[moves-1])
                    entity.action_points -= moves
