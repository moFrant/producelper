"""Парсинг пользовательского ввода."""
from producelper.base.note import Note, NoteC, NoteCSharp, NoteDFlat, NoteBSharp, NoteD, NoteDSharp, NoteEFlat, NoteE, \
    NoteFFlat, NoteESharp, NoteF, NoteFSharp, NoteGFlat, NoteG, NoteGSharp, NoteAFlat, NoteA, NoteASharp, NoteBFlat, \
    NoteB, NoteCFlat
from producelper.base.scale import Scale, MajorScale, MinorScale


def parse_key(user_key: str) -> tuple[Note, Scale]:
    """Парсинг пользовательского ввода тональности."""

    if len(user_key) == 1 or user_key[-1] != 'm':
        scale = MajorScale()  # Одним символом всегда задается мажорная тональность
        key = user_key
    elif len(user_key) == 3 or user_key[-1] == 'm':
        scale = MinorScale()  # Тремя символами всегда задается минорная тональность
        key = user_key[:-1]
    else:
        raise  # Не правильный пользовательский ввод

    return get_notes().get(key), scale


def get_notes() -> dict[str, Note]:
    """Получить словарь всех нот."""

    results: dict[str, Note] = {}

    notes: list[tuple[Note, Note] | Note] = [
        (NoteC(), NoteBSharp()),
        (NoteCSharp(), NoteDFlat()),
        NoteD(),
        (NoteDSharp(), NoteEFlat()),
        (NoteE(), NoteFFlat()),
        (NoteESharp(), NoteF()),
        (NoteFSharp(), NoteGFlat()),
        NoteG(),
        (NoteGSharp(), NoteAFlat()),
        NoteA(),
        (NoteASharp(), NoteBFlat()),
        (NoteB(), NoteCFlat())
    ]

    for note in notes:
        if isinstance(note, tuple):
            for _note in note:
                results[_note.get_name()] = _note
        else:
            results[note.get_name()] = note

    return results
