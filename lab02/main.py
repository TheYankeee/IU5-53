from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
from lab_python_oop.rect import Rect


def main():
    r = Rect(2, 3, *(100, 0, 200))
    c = Circle(5, *(0, 200, 100))
    s = Square(4, *(200, 100, 0))
    print('Фигуры:\n{}\n{}\n{}'.format(s, c, r))


if __name__ == "__main__":
    main()
