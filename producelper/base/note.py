"""Ноты."""
from abc import ABC, abstractmethod


class Note(ABC):
    """Интерфейс ноты."""

    index_key: int  # Индекс клавиши, на которой находится.

    @abstractmethod
    def get_name(self) -> str:
        """Получить название ноты."""

    def __str__(self) -> str:
        return self.get_name()


class NoteC(Note):
    """Нота ДО."""

    index_key = 0

    def get_name(self) -> str:
        return 'C'


class NoteCSharp(Note):
    """Нота ДО Диез."""

    index_key = 1

    def get_name(self) -> str:
        return 'C#'


class NoteDFlat(Note):
    """Нота РЕ Бемоль."""

    index_key = 1

    def get_name(self) -> str:
        return 'Db'


class NoteD(Note):
    """Нота РЕ."""

    index_key = 2

    def get_name(self) -> str:
        return 'D'


class NoteDSharp(Note):
    """Нота РЕ Диез."""

    index_key = 3

    def get_name(self) -> str:
        return 'D#'


class NoteEFlat(Note):
    """Нота МИ Бемоль."""

    index_key = 3

    def get_name(self) -> str:
        return 'Eb'


class NoteE(Note):
    """Нота МИ."""

    index_key = 4

    def get_name(self) -> str:
        return 'E'


class NoteESharp(Note):
    """Нота МИ Диез."""

    index_key = 5

    def get_name(self) -> str:
        return 'E#'


class NoteFFlat(Note):
    """Нота ФА Бемоль."""

    index_key = 4

    def get_name(self) -> str:
        return 'Fb'


class NoteF(Note):
    """Нота ФА."""

    index_key = 5

    def get_name(self) -> str:
        return 'F'


class NoteFSharp(Note):
    """Нота ФА Диез."""

    index_key = 6

    def get_name(self) -> str:
        return 'F#'


class NoteGFlat(Note):
    """Нота СОЛЬ Бемоль."""

    index_key = 6

    def get_name(self) -> str:
        return 'Gb'


class NoteG(Note):
    """Нота СОЛЬ."""

    index_key = 7

    def get_name(self) -> str:
        return 'G'


class NoteGSharp(Note):
    """Нота СОЛЬ Диез."""

    index_key = 8

    def get_name(self) -> str:
        return 'G#'


class NoteAFlat(Note):
    """Нота ЛЯ Бемоль."""

    index_key = 8

    def get_name(self) -> str:
        return 'Ab'


class NoteA(Note):
    """Нота ЛЯ."""

    index_key = 9

    def get_name(self) -> str:
        return 'A'


class NoteASharp(Note):
    """Нота ЛЯ Диез."""

    index_key = 10

    def get_name(self) -> str:
        return 'A#'


class NoteBFlat(Note):
    """Нота СИ Бемоль."""

    index_key = 10

    def get_name(self) -> str:
        return 'Bb'


class NoteB(Note):
    """Нота СИ."""

    index_key = 11

    def get_name(self) -> str:
        return 'B'


class NoteBSharp(Note):
    """Нота СИ Диез."""

    index_key = 0

    def get_name(self) -> str:
        return 'B#'


class NoteCFLat(Note):
    """Нота ДО Бемоль."""

    index_key = 11

    def get_name(self) -> str:
        return 'Cb'
