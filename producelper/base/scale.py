"""Лады"""
from abc import ABC

TONE = 2
SEMITONE = 1
TONIC = 0


class Scale(ABC):
    """Интерфейс для лада."""

    tones: dict[int, int]  # Распределение тонов и полутонов в ладу.


class ChromaticScale(Scale):
    """Хроматический лад"""

    tones = {
        1: TONIC,
        2: SEMITONE,
        3: SEMITONE,
        4: SEMITONE,
        5: SEMITONE,
        6: SEMITONE,
        7: SEMITONE,
        8: SEMITONE,
        9: SEMITONE,
        10: SEMITONE,
        11: SEMITONE,
        12: SEMITONE
    }


class MajorScale(Scale):
    """Мажорный лад."""

    tones = {
        1: TONIC,
        2: TONE,
        3: TONE,
        4: SEMITONE,
        5: TONE,
        6: TONE,
        7: TONE
    }

    def __str__(self) -> str:
        return 'major'


class MinorScale(Scale):
    """Минорный лад."""

    tones = {
        1: TONIC,
        2: TONE,
        3: SEMITONE,
        4: TONE,
        5: TONE,
        6: SEMITONE,
        7: TONE
    }

    def __str__(self) -> str:
        return 'minor'
