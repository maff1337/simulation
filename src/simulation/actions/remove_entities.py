from simulation.actions.action import Action
from simulation.entities import Creature
from simulation.world import World


class RemoveEntitiesAction(Action):
    def perform(self, world: World) -> None:
        to_remove = []

        for entity in world.get_entities():
            if isinstance(entity, Creature):
                if entity.hp <= 0:
                    to_remove.append(entity)

        for entity in to_remove:
            world.delete_entity(entity)
