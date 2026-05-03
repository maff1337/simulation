from simulation.entities import Entity, Fox, Grass, Mountain, Rabbit, Tree


class Factory:
    mapping = {
        'fox': Fox,
        'rabbit': Rabbit,
        'mountain': Mountain,
        'tree': Tree,
        'grass': Grass
    }

    def __init__(self, attributes: dict) -> None:
        self._attributes = attributes

    def create(self, name: str) -> Entity:
        entity_class = self.mapping.get(name)

        if entity_class is None:
            raise

        return entity_class(**self._attributes[name])
