from abc import ABC


class Entity(ABC):
    def __str__(self) -> str:
        return f'{self.__class__.__name__.capitalize()}()'

    def __repr__(self) -> str:
        return str(self)


class Creature(Entity, ABC):
    def __init__(self, hp: int, speed: int) -> None:
        self._hp = hp
        self._speed = speed

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = value

        if self._hp < 0:
            self._hp = 0

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, value: int) -> None:
        self._speed = value


class StaticEntity(Entity, ABC):
    ...


class Herbivore(Creature, ABC):
    def __str__(self) -> str:
        return f'{self.__class__.__name__.capitalize()}(hp={self.hp}, speed={self.speed})'


class Carnivore(Creature, ABC):
    def __init__(self, hp: int, speed: int, attack: int) -> None:
        super().__init__(hp, speed)

        self._attack = attack

    @property
    def attack(self) -> int:
        return self._attack

    def bite(self, herbivore: Herbivore) -> None:
        herbivore.hp -= (self.attack * self.speed)

    def __str__(self) -> str:
        return f'{self.__class__.__name__.capitalize()}(hp={self.hp}, speed={self.speed}, attack={self.attack})'


class Resource(StaticEntity, ABC):
    ...


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
