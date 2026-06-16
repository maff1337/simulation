from simulation.world import World
from simulation.coordinates import Coordinates
from simulation.renderers.renderer import Renderer


class CliRenderer(Renderer):
    def __init__(self, world: World, icons: dict, phrases: dict) -> None:
        self._world = world

        self._icons = icons
        self._phrases = phrases

    def update_phrases(self, phrases: dict) -> None:
        self._phrases = phrases

    def render_turn(self, step: int) -> None:
        for row in range(self._world.rows):
            for column in range(self._world.columns):
                coords = Coordinates(row, column)

                entity = self._world.get_entity(coords)

                if entity is not None:
                    name = entity.__class__.__name__.lower()
                    print(self._icons.get(name), end=' ')
                else:
                    print(self._icons.get('ceil'), end=' ')
            print()
        print(self._phrases['menu']['turn']['step'].format(step=step))
        print()

    def render_main_menu(self) -> None:
        print(self._phrases['menu']['main']['welcome'])
        print(self._phrases['menu']['main']['menu_options'])
        print(self._phrases['menu']['main']['prompt'], end='')

    def render_ongoing_menu(self) -> None:
        print(self._phrases['menu']['ongoing']['prompt'])
        print(self._phrases['menu']['ongoing']['menu_options'])
        print()

    def render_onpause_menu(self) -> None:
        print(self._phrases['menu']['onpause']['prompt'])
        print(self._phrases['menu']['onpause']['menu_options'])
        print()

    def render_language_menu(self) -> None:
        print(self._phrases['menu']['language']['prompt'], end='')

    def render_goodbye(self) -> None:
        print(self._phrases['menu']['main']['goodbye'])

    def render_invalid_choice(self) -> None:
        print(self._phrases['error_messages']['invalid_input'])
