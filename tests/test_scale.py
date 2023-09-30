"""Тестирование ладов."""
from producelper.base.button import OctaveBase
from producelper.base.note import NoteC, NoteAFlat
from producelper.base.scale import MajorScale, MinorScale


def test_major():
    """Тестирование мажорного лада."""

    octave = OctaveBase()
    octave.set_root(NoteC())
    octave.set_scale(MajorScale())

    assert str(octave) == '1(T) - 2 - 3(D) 4 - 5(SD) - 6 - 7'

    octave = OctaveBase(root_note=NoteAFlat(), scale=MajorScale())
    assert str(octave) == '3(D) 4 - 5(SD) - 6 - 7 1(T) - 2 -'


def test_minor():
    """Тестирование минорного лада."""

    octave = OctaveBase(root_note=NoteC(), scale=MinorScale())
    assert str(octave) == '1(T) - 2 3(D) - 4 - 5(SD) 6 - 7 -'

    octave = OctaveBase(root_note=NoteAFlat(), scale=MinorScale())
    assert str(octave) == '- 4 - 5(SD) 6 - 7 - 1(T) - 2 3(D)'
