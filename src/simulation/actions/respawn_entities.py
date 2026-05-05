from math import ceil
from random import random

from simulation.actions.action import Action
from simulation.factory import Factory
from simulation.world import World


class RespawnEntitesAction(Action):
    def __init__(self, coeffs: dict, factory: Factory) -> None:
        self._coeffs = coeffs
        self._factory = factory

    def perform(self, world: World) -> None:
        for entity_name in self._factory.mapping.keys():
            respawn_coeff = self._coeffs[entity_name]['respawn']
            respawn_chance = self._coeffs[entity_name]['respawn_chance']

            for _ in range(ceil(respawn_coeff * world.size())):
                chance = random()
                if chance > respawn_chance:
                    world.add_entity(self._factory.create(entity_name))
