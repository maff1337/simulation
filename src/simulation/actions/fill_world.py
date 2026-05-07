from math import ceil
from random import random

from simulation.world import World
from simulation.factory import Factory
from simulation.actions.action import Action


class FillWorldAction(Action):
    def __init__(self, coeffs: dict, factory: Factory) -> None:
        self._coeffs = coeffs
        self._factory = factory

    def perform(self, world: World) -> None:
        for entity_name in self._factory.mapping.keys():
            spawn_coeff = self._coeffs[entity_name]['spawn']
            spawn_chance = self._coeffs[entity_name]['spawn_chance']

            for _ in range(ceil(spawn_coeff * world.size())):
                chance = random()
                if chance > spawn_chance:
                    world.add_entity(self._factory.create(entity_name))
