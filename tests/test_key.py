"""Тестирование тональностей."""
import pytest

from producelper.base.note import NoteG, NoteA, NoteDSharp, NoteFSharp, NoteCFlat, NoteBFlat
from producelper.base.scale import MajorScale, MinorScale
from producelper.key.parser import parse_key


@pytest.mark.parametrize('key, note, scale', (
        ('G', NoteG, MajorScale),
        ('Am', NoteA, MinorScale),
        ('D#', NoteDSharp, MajorScale),
        ('Cb', NoteCFlat, MajorScale),
        ('F#m', NoteFSharp, MinorScale),
        ('Bbm', NoteBFlat, MinorScale)
))
def test_parse_user_key(key, note, scale):
    """Тестирование парсинга пользовательского ввода тональности."""

    parsed_key, parsed_scale = parse_key(key)
    assert isinstance(parsed_key, note)
    assert isinstance(parsed_scale, scale)
