"""Консольное приложение."""
from producelper.console_app import AppBase
from producelper.key.console_app import KeyApp


class MainApp(AppBase):
    """Главное приложение."""

    def help(self, *args) -> None:
        print()
        print("help - вывести справку, exit - выход из программы")
        print("key - перейти в подситему работы с тональностями.")
        print()

    def starting_message(self) -> None:
        print("Программа-помощник создания музыки.")


def main():
    """Основной поток приложения."""

    main_app = MainApp()
    key_app = KeyApp()

    main_app.register_app('key', key_app)
    main_app.run()


if __name__ == "__main__":
    main()
