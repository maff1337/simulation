from abc import abstractmethod
from typing import Protocol


class Renderer(Protocol):
    @abstractmethod
    def update_phrases(self, phrases: dict) -> None: ...

    @abstractmethod
    def render_turn(self, step: int) -> None: ...

    @abstractmethod
    def render_main_menu(self) -> None: ...

    @abstractmethod
    def render_ongoing_menu(self) -> None: ...

    @abstractmethod
    def render_onpause_menu(self) -> None: ...

    @abstractmethod
    def render_language_menu(self) -> None: ...

    @abstractmethod
    def render_goodbye(self) -> None: ...

    @abstractmethod
    def render_invalid_choice(self) -> None: ...
