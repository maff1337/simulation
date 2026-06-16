from time import sleep
from pathlib import Path
from typing import Sequence
from threading import Event, Thread

from simulation.world import World
from simulation.actions.action import Action
from simulation.configs.config import Config
from simulation.renderers.renderer import Renderer
from simulation.commands import LanguageMenuCommands, MainMenuCommands, OngoingMenuCommands, OnpauseMenuCommands


class Simulation:
    def __init__(
        self,
        initial: Sequence[Action],
        turn: Sequence[Action],
        world: World,
        renderer: Renderer,
        language: str,
        configs: Config
    ) -> None:
        self._step = 0

        self._initial_actions = initial
        self._turn_actions = turn

        self._world = world
        self._renderer = renderer

        self._language = language
        self._configs = configs

        self._ongoing = Event()
        self._stopped = Event()

    def next_turn(self) -> None:
        for action in self._turn_actions:
            action.perform(self._world)

    def start_simulation(self, ongoing: Event, stopped: Event) -> None:
        for action in self._initial_actions:
            action.perform(self._world)

        while not stopped.is_set():
            ongoing.wait()

            self._renderer.render_turn(self._step)
            self._renderer.render_ongoing_menu()

            self.next_turn()
            self._step += 1

            sleep(1.5)

    def main_menu(self) -> None:
        while True:
            self._renderer.render_main_menu()
            choice = input()

            match choice:
                case MainMenuCommands.FIRST.value:
                    self._stopped.clear()
                    self._ongoing.set()

                    subthread = Thread(
                        target=self.start_simulation,
                        args=(self._ongoing, self._stopped),
                        daemon=True
                    )

                    subthread.start()

                    while True:
                        if not self._ongoing.is_set():
                            self._renderer.render_onpause_menu()

                        cmd = input()

                        if self._ongoing.is_set():
                            match cmd:
                                case OngoingMenuCommands.FIRST.value:
                                    self._ongoing.clear()
                                case OngoingMenuCommands.SECOND.value:
                                    self._stopped.set()
                                    self._ongoing.set()
                                    self._renderer.render_goodbye()
                                    return
                        else:
                            match cmd:
                                case OnpauseMenuCommands.FIRST.value:
                                    self._ongoing.set()
                                case OnpauseMenuCommands.SECOND.value:
                                    self._stopped.set()
                                    self._ongoing.set()
                                    self._renderer.render_goodbye()
                                    return

                case MainMenuCommands.SECOND.value:
                    self.select_language()
                case MainMenuCommands.THIRD.value:
                    self._renderer.render_goodbye()
                    break
                case _:
                    self._renderer.render_invalid_choice()

    def select_language(self) -> None:
        while True:
            self._renderer.render_language_menu()
            choice = input()

            language = LanguageMenuCommands.get_language(choice)
            if language:
                self._language = language
                path = Path(self._configs.get('locales').get(language))
                locales = Config(path)

                self._renderer.update_phrases(locales._config)

                break
            else:
                self._renderer.render_invalid_choice()
