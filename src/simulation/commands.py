from enum import Enum


class MainMenuCommands(Enum):
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'


class OngoingMenuCommands(Enum):
    FIRST = '1'
    SECOND = '2'


class OnpauseMenuCommands(Enum):
    FIRST = '1'
    SECOND = '2'


class LanguageMenuCommands:
    language = {
        '1': 'ru',
        '2': 'en'
    }

    @classmethod
    def get_language(cls, choice: str) -> str | None:
        return cls.language.get(choice, None)
