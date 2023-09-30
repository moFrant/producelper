"""Консольное приложение для работы с тональностями."""
from producelper.base.button import OctaveBase
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
        print()
        print("Например, `info C#`")
        print()
        print("Если интересуют весь лад, то можно использовать следующую команду `info . <major|minor>`")
        print()
        print("Если нужно вывести какие клавиши участруют в тональности, то используйте команду scale с указанием "
              "какую тональность нужно показать")
        print("Клавиши идут по порядку, учитывая белые и черные клавиши. * обозначает, что клавиша участвует в "
              "тональности")
        print()
        print("Например, `scale F#`")
        print()
        print("Если нужно вывести более детальную информацию, то в конце укажите v, например, `scale A v`")
        print("В данном режиме выходит порядковый номер ступени, а так же краткое описание роли ступени.")
        print("T - тоника, D - доминанта, SD - субдоминанта. Клавиши без ролей являются не устойчивыми.")
        print()

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

    @staticmethod
    def scale(key: str, detail: str | None = None) -> None:
        """Показать информацию по тональности."""

        if detail and detail != 'v':
            raise  # Нераспозн уровень детализации.

        note, scale = parse_key(key)
        octave = OctaveBase(root_note=note, scale=scale)

        if detail:
            info = octave.get_info_keys(False)
        else:
            info = octave.get_info_keys()

        print(' '.join(info))
