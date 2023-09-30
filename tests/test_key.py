"""Тестирование тональностей."""
import pytest

from producelper.base.note import NoteG, NoteA, NoteDSharp, NoteFSharp, NoteCFlat, NoteBFlat, NoteE, NoteFFlat, NoteB, \
    NoteD
from producelper.base.scale import MajorScale, MinorScale
from producelper.key.description import description, get_descriptions
from producelper.key.parser import parse_key


key_description = description

key_major_description = description.copy()
key_major_description.pop('minor')

key_minor_description = description.copy()
key_minor_description.pop('major')


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


@pytest.mark.parametrize('key, scale, key_description', (
        (None, None, key_description),
        (None, MajorScale(), key_major_description),
        (None, MinorScale(), key_minor_description),
        (NoteE(), None, {'major': {'E | Fb': 'Сияющий'}, 'minor': {'E | Fb': 'Светлый'}}),
        (NoteFFlat(), None, {'major': {'E | Fb': 'Сияющий'}, 'minor': {'E | Fb': 'Светлый'}}),
        (NoteB(), MajorScale(), {'major': {'B | Cb': 'Могучий'}}),
        (NoteCFlat(), MajorScale(), {'major': {'B | Cb': 'Могучий'}}),
        (NoteD(), MinorScale(), {'minor': {'D': 'Мужественный'}})
))
def test_get_description(key, scale, key_description):
    """Тестирование получение описание тональности."""

    assert get_descriptions(key, scale) == key_description
