from lab_python_oop.figure_color import FigureColor
from lab_python_oop.rect import Rect

class Square(Rect):
    def __init__(self):
        super().__init__()

    def __init__(self, line: int):
        super().__init__(line, line)

    def __init__(self, line: int, color: FigureColor):
        super().__init__(line, line, color)

    def __init__(self, line: int, red: int, green: int, blue: int):
        super().__init__(line, line, red, green, blue)

    def __repr__(self) -> str:
        return 'Квадрат цвета {}; со стороной {}; площадью {}.'.format(
            self.figure_color,
            self.height,
            self.area()
        )