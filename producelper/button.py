"""Клавиши контроллера."""
from abc import ABC, abstractmethod

from producelper.note import Note
from producelper.scale import Scale


class Key(ABC):
    """Клавиша контроллера."""

    tonic: bool | None
    step: int | None
    enabled: bool

    @abstractmethod
    def set_tonic(self) -> None:
        """Сделать клавишу тоникой."""

    @abstractmethod
    def set_step(self, index: int) -> None:
        """Установить номер ступени."""

    @abstractmethod
    def disable(self) -> None:
        """Деактивировать клавишу."""

    @abstractmethod
    def enable(self) -> None:
        """Активировать клавишу"""


class KeyBase(Key):
    """Базовый класс для клавиши контроллера."""

    def __init__(self):
        self.tonic = None
        self.step = None
        self.enable()

    def set_tonic(self) -> None:
        self.tonic = True
        self.set_step(1)

    def set_step(self, index: int) -> None:
        if index != 1:
            self.tonic = False

        self.step = index

    def disable(self) -> None:
        self.enabled = False

    def enable(self) -> None:
        self.enabled = True


class KeyC(KeyBase):
    """Клавиша С."""


class KeyCD(KeyBase):
    """Клавиша C# или Db."""


class KeyD(KeyBase):
    """Клавиша D."""


class KeyDE(KeyBase):
    """Клавиша D# или Eb."""


class KeyE(KeyBase):
    """Клавиша E."""


class KeyF(KeyBase):
    """Клавиша F."""


class KeyFG(KeyBase):
    """Клавиша F# или Gb."""


class KeyG(KeyBase):
    """Клавиша G."""


class KeyGA(KeyBase):
    """Клавиша G# или Ab."""


class KeyA(KeyBase):
    """Клавиша A."""


class KeyAB(KeyBase):
    """Клавиша A# или Bb."""


class KeyB(KeyBase):
    """Клавиша B."""


class Octave(ABC):
    """Интерфейс для октавы контролера."""

    index: int  # Номер октавы
    root: Note | None  # Ключеная нота, от нее строится тоника.
    keys: tuple[Key]  # Клавиши
    scale: Scale | None  # Установленный лад

    @abstractmethod
    def set_root(self, note: Note | None) -> None:
        """Установить ключеную ноту."""

    @abstractmethod
    def disable_all(self) -> None:
        """Деактивировать все клавиши."""

    @abstractmethod
    def enable_all(self) -> None:
        """Активировать все клавиши"""

    @abstractmethod
    def set_scale(self, scale: Scale | None) -> None:
        """Установить лад."""

    def get_info_keys(self, simple: bool = True) -> list[str]:
        """Получить информацию по клавишам в октаве."""

        result = []
        for key in self.keys:
            if key.enabled:
                if simple or key.step is None:
                    result.append('*')
                else:
                    additional = ''
                    if key.tonic:
                        additional = '(T)'
                    elif key.step == 3:
                        additional = '(D)'
                    elif key.step == 5:
                        additional = '(SD)'
                    result.append(f"{key.step}{additional}")
            else:
                result.append('-')

        return result

    def __str__(self) -> str:
        return ' '.join(self.get_info_keys(simple=False))


class OctaveBase(Octave):
    """Базовый класс для октавы."""

    keys: tuple[Key] = (
        KeyC(),
        KeyCD(),
        KeyD(),
        KeyDE(),
        KeyE(),
        KeyF(),
        KeyFG(),
        KeyG(),
        KeyGA(),
        KeyA(),
        KeyAB(),
        KeyB()
    )

    def __init__(self, index: int = 0, root_note: Note | None = None, scale: Scale | None = None) -> None:
        self.index = index
        self.set_root(root_note)
        self.set_scale(scale)

    def set_root(self, note: Note | None) -> None:
        self.root = note
        if not note:
            self.enable_all()
            return

        self.keys[self.root.index_key].set_tonic()

    def disable_all(self) -> None:
        for key in self.keys:
            key.disable()

    def enable_all(self) -> None:
        for key in self.keys:
            key.enable()

    def set_scale(self, scale: Scale | None) -> None:

        self.scale = scale
        if not scale:
            self.enable_all()
        else:
            if not self.root:
                raise  # Нужно вначале задать тонику.

            self.disable_all()
            keys = list(self.keys)
            for _ in range(self.root.index_key):
                key = keys.pop(0)
                keys.append(key)

            index = 0
            for step, interval in scale.tones.items():
                index += interval
                key = keys[index]
                key.enable()
                key.set_step(step)
