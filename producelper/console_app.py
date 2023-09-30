"""Объекты для работы консольного приложения."""
from abc import ABC, abstractmethod


class App(ABC):
    """Консольное приложение."""

    full_command: str | None

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
        print()
        self.starting_message()
        while not self._exit:
            self.full_command = command = input("Введите команду: ")

            try:
                self.execute_command(command)
            except Exception as exc:
                print(f"Произошла ошибка {exc}")

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
            self.full_command = None
            return

        key_command = parsed_command.pop(0)
        app = self.apps.get(key_command)
        if app:
            if parsed_command:
                app.full_command = self.full_command
                self.full_command = None
                return app.execute_command(self.get_command(parsed_command))
            else:
                self.full_command = None
                try:
                    return app.run()
                finally:
                    self.starting_message()

        method = getattr(self, key_command)
        if method:
            try:
                return method(*parsed_command)
            finally:
                self.full_command = None

        self.full_command = None
        raise  # Не удалось определить команду
