from lab_python_oop.figure_color import FigureColor
from lab_python_oop.figure import Figure

import math


class Circle(Figure):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def __init__(self, radius, color: FigureColor):
        super().__init__(color)
        self.radius = radius

    def __init__(self, radius, red: int, green: int, blue: int):
        super().__init__(red, green, blue)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ^ 2)

    def __repr__(self) -> str:
        return 'Круг цвета {}; радиусом {}; площадью {}.'.format(
            self.figure_color,
            self.radius,
            self.area()
        )