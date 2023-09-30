"""Описание тональностей."""
from producelper.base.note import Note
from producelper.base.scale import Scale, MajorScale, MinorScale

tonic_map: dict[str, str] = {
    'C': 'C | B#',
    'B#': 'C | B#',
    'C#': 'C# | Db',
    'Db': 'C# | Db',
    'D': 'D',
    'D#': 'D# | Eb',
    'Eb': 'D# | Eb',
    'E': 'E | Fb',
    'Fb': 'E | Fb',
    'E#': 'E# | F',
    'F': 'E# | F',
    'F#': 'F# | Gb',
    'Gb': 'F# | Gb',
    'G': 'G',
    'G#': 'G# | Ab',
    'Ab': 'G# | Ab',
    'A': 'A',
    'A#': 'A# | Bb',
    'Bb': 'A# | Bb',
    'B': 'B | Cb',
    'Cb': 'B | Cb'
}


description: dict[str, dict[str, str]] = {
    'major': {
        'C | B#': 'Твердый, решительный',
        'C# | Db': 'Важный',
        'D': 'Блестящий',
        'D# | Eb': 'Величественный',
        'E | Fb': 'Сияющий',
        'E# | F': 'Мужественный',
        'F# | Gb': 'Жесткий | Мрачный',
        'G': 'Веселый',
        'G# | Ab': 'Благородный',
        'A': 'Радостный',
        'A# | Bb': 'Гордый',
        'B | Cb': 'Могучий'
    },
    'minor': {
        'C | B#': 'Патетический',
        'C# | Db': 'Элегический',
        'D': 'Мужественный',
        'D# | Eb': 'Высокая тональность | Суровый',
        'E | Fb': 'Светлый',
        'E# | F': 'Печальный',
        'F# | Gb': 'Взволнованный',
        'G': 'Поэтический',
        'G# | Ab': 'Напряженный',
        'A': 'Легкий',
        'A# | Bb': 'Сумрачный',
        'B | Cb': 'Скорбный'
    }
}


def get_descriptions(note: Note | None = None, scale: Scale | None = None) -> dict[str, dict[str, str]]:
    """Получить описание тональностей. Возможно отфильтровать по минору или мажору, а так же по ключевой ноте."""

    _description = description.copy()

    if note:
        key = tonic_map[note.get_name()]
        _description = {
            'major': {
                key: description['major'][key]
            },
            'minor': {
                key: description['minor'][key]
            }
        }

    if scale:
        if isinstance(scale, MajorScale):
            _description.pop(str(MinorScale()))
        elif isinstance(scale, MinorScale):
            _description.pop(str(MajorScale()))

    return _description
