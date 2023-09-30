"""Консольное приложение для работы с тональностями."""
from producelper.base.scale import MajorScale, MinorScale
from producelper.console_app import AppBase
from producelper.key.description import get_descriptions
from producelper.key.parser import parse_key


class KeyApp(AppBase):
    """Консольное приложение для работы с тональностями."""

    def help(self, *args) -> None:
        print("Справка по работе с тональностями.")
        print("Чтобы получить информацию по всем тональностям и их названия используйте команду `info`")
        print("Так же можно уточнить какая именно тональность интересует, для этого укажите название этой тональности.")
        print("Например, `info C#`")
        print("Если интересуют весь лад, то можно использовать следующую команду `info . <major|minor>`")

    def starting_message(self) -> None:
        print("Информация по тональностям.")

    @staticmethod
    def _print_description(descriptions: dict[str, dict[str, str]]) -> None:
        """Вспомогательный метод, чтобы красиво вывести описание в консоль."""

        print()
        for scale, info in descriptions.items():
            print(f"{scale}:")
            for note, description in info.items():
                print(f"{note}: {description}")
            print()

    def info(self, key: str | None = None, scale: str | None = None) -> None:
        """Вывести информацию по тональностям"""

        if key and key != '.':
            note, scale = parse_key(key)
        elif scale:
            if scale == 'major':
                note, scale = None, MajorScale()
            elif scale and scale == 'minor':
                note, scale = None, MinorScale()
            else:
                raise  # Не удалось определить лад.
        else:
            note, scale = None, None

        descriptions = get_descriptions(note, scale)
        return self._print_description(descriptions)
