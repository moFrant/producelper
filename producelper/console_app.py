"""Объекты для работы консольного приложения."""
from abc import ABC, abstractmethod


class App(ABC):
    """Консольное приложение."""

    @abstractmethod
    def help(self, *args) -> None:
        """Вывести справку."""

    @abstractmethod
    def starting_message(self) -> None:
        """Вывод начального привествия. Можно ничего не выводить"""

    @abstractmethod
    def run(self) -> None:
        """Запуск консольного приложения."""

    @abstractmethod
    def register_app(self, command: str, app: 'App') -> None:
        """Регистрация вложенного приложения."""

    @abstractmethod
    def execute_command(self, command: str) -> None:
        """Выполнить команду"""


class AppBase(App, ABC):
    """Базовый класс для консольного приложения."""

    def __init__(self):
        self.full_command: str | None = None
        self._exit: bool = False
        self.apps: dict[str, App] = {}

    def exit(self) -> None:
        """Команда выхода из приложения."""

        self._exit = True
        self.full_command = None

    def register_app(self, command: str, app: 'App') -> None:
        self.apps[command] = app

    def run(self) -> None:
        self.starting_message()
        while not self._exit:
            self.full_command = command = input("Введите команду: ")
            self.execute_command(command)

        self._exit = False

    @staticmethod
    def parse_command(command: str) -> list[str]:
        """Пасит команду, разбивая на слова."""

        return command.split()

    @staticmethod
    def get_command(commands: list[str]) -> str:
        """Преобразует из разобранных команд одну команду для передачи дальше."""

        return ' '.join(commands)

    def execute_command(self, command: str) -> None:
        parsed_command = self.parse_command(command)
        if not parsed_command:
            return

        key_command = parsed_command.pop(0)
        app = self.apps.get(key_command)
        if app:
            if parsed_command:
                return app.execute_command(self.get_command(parsed_command))
            else:
                return app.run()

        method = getattr(self, key_command)
        if method:
            return method(*parsed_command)

        raise  # Не удалось определить команду
