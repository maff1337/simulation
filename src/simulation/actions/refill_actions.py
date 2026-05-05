from simulation.actions.action import Action
from simulation.entities import Creature
from simulation.factory import Factory
from simulation.world import World


class RefillActionPointsAction(Action):
    def __init__(self, attributes: dict) -> None:
        self._attributes = attributes

    def perform(self, world: World) -> None:
        for entity in world.get_entities():
            if isinstance(entity, Creature):
                name = entity.__class__.__name__.lower()

                entity.action_points = self._attributes[name]['action_points']
