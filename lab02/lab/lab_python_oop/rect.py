from lab_python_oop.figure import Figure
from lab_python_oop.figure_color import FigureColor

class Rect(Figure):
    def __init__(self):
        super().__init__()
        self.height = 0
        self.width = 0

    def __init__(self, height: int, width: int):
        super().__init__()
        self.height = height
        self.width = width

    def __init__(self, height: int, width: int, color: FigureColor):
        super().__init__(color)
        self.height = height
        self.width = width

    def __init__(self, height: int, width: int, red: int, green: int, blue: int):
        super().__init__(red, green, blue)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def __repr__(self) -> str:
        return 'Прямоугольник цвета {}; размером {}x{}; площадью {}.'.format(
            self.figure_color,
            self.height,
            self.width,
            self.area()
        )