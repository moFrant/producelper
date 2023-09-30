"""Консольное приложение."""


def main():
    """Основной поток приложения."""

    print("Помощник по созданию музыки.")
    print("help помощь по командам. exit выход из проложения.")
    end = False
    while not end:
        command = input("Введите команду - ")
        if command == 'exit':
            end = True
            continue


if __name__ == "__main__":
    main()
