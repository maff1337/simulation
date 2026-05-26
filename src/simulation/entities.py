from abc import ABC
from typing import Type


class Entity(ABC):
    target: Type['Entity']

    def __str__(self) -> str:
        return f'{self.__class__.__name__.capitalize()}()'

    def __repr__(self) -> str:
        return str(self)


class Creature(Entity, ABC):
    def __init__(self, hp: int, action_points: int, attack: int) -> None:
        self._hp = hp
        self._action_points = action_points
        self._attack = attack

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = value

        if self._hp < 0:
            self._hp = 0

    @property
    def action_points(self) -> int:
        return self._action_points

    @action_points.setter
    def action_points(self, value: int) -> None:
        self._action_points = value

    @property
    def attack(self) -> int:
        return self._attack

    def bite(self, other) -> None:
        if isinstance(other, self.target):
            other.hp -= self.attack  # type: ignore

    def __str__(self) -> str:
        return f'{self.__class__.__name__.capitalize()}(hp={self.hp}, action_points={self.action_points}, attack={self.attack})'


class StaticEntity(Entity, ABC):
    ...


class Resource(StaticEntity, ABC):
    def __init__(self, hp: int) -> None:
        self._hp = hp

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = value

        if self._hp < 0:
            self._hp = 0


class Herbivore(Creature, ABC):
    target = Resource


class Carnivore(Creature, ABC):
    target = Herbivore


class Fox(Carnivore):
    ...


class Rabbit(Herbivore):
    ...


class Grass(Resource):
    ...


class Mountain(StaticEntity):
    ...


class Tree(StaticEntity):
    ...
