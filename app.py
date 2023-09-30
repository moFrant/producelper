"""Консольное приложение."""
from producelper.console_app import AppBase


class MainApp(AppBase):
    """Главное приложение."""

    def help(self, *args) -> None:
        print("help - вывести справку, exit - выход из программы")

    def starting_message(self) -> None:
        print("Программа-помощник создания музыки.")


def main():
    """Основной поток приложения."""

    main_app = MainApp()
    main_app.run()


if __name__ == "__main__":
    main()
