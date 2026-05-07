from typing import Protocol
from abc import abstractmethod

from simulation.world import World


class Action(Protocol):
    @abstractmethod
    def perform(self, world: World) -> None:
        ...
