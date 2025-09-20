from colorama import init, Fore, Back, Style
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    init(autoreset=True)

    N = 24

    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "ДЕМОНСТРАЦИЯ РАБОТЫ С ГЕОМЕТРИЧЕСКИМИ ФИГУРАМИ")
    print(Fore.CYAN + "=" * 60)

    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    print(Fore.GREEN + "\nИнформация о фигурах:")
    print(Fore.WHITE + f"1. {rectangle}")
    print(Fore.WHITE + f"2. {circle}")
    print(Fore.WHITE + f"3. {square}")

    print(Fore.MAGENTA + "\n" + "=" * 60)
    print(Fore.YELLOW + "ДЕМОНСТРАЦИЯ ВНЕШНЕГО ПАКЕТА COLORAMA")
    print(Fore.MAGENTA + "=" * 60)

    print(Fore.RED + "Красный текст")
    print(Back.GREEN + "Зеленый фон")
    print(Style.BRIGHT + Fore.BLUE + "Яркий синий текст")
    print(Fore.YELLOW + Back.BLUE + "Желтый текст на синем фоне")

    print(Fore.CYAN + "\nПрограмма завершена успешно!")

if __name__ == "__main__":
    main()
