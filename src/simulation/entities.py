from abc import ABC, abstractmethod
from typing import Type


class Entity(ABC):
    target: Type['Entity']

    def __str__(self) -> str:
        return f'{self.__class__.__name__.capitalize()}()'

    def __repr__(self) -> str:
        return str(self)


class Creature(Entity, ABC):
    def __init__(self, hp: int, action_points: int) -> None:
        self._hp = hp
        self._action_points = action_points

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

    @abstractmethod
    def bite(self, other) -> None:
        ...


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

    def __str__(self) -> str:
        return f'{self.__class__.__name__.capitalize()}(hp={self.hp}, action_points={self.action_points})'

    def bite(self, other: Resource) -> None:
        other.hp = 0

        self.action_points -= 1


class Carnivore(Creature, ABC):
    target = Herbivore

    def __init__(self, hp: int, action_points: int, attack: int) -> None:
        super().__init__(hp, action_points)

        self._attack = attack

    @property
    def attack(self) -> int:
        return self._attack

    def bite(self, other: Herbivore) -> None:
        hits = other.hp // self.attack + (other.hp % self.attack != 0)

        if hits <= self.action_points:
            other.hp -= (self.attack * hits)

            self.action_points -= hits
        else:
            other.hp -= (self.attack * self.action_points)

            self.action_points = 0

    def __str__(self) -> str:
        return f'{self.__class__.__name__.capitalize()}(hp={self.hp}, action_points={self.action_points}, attack={self.attack})'


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
