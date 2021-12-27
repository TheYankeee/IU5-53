from abc import ABC, abstractmethod, abstractproperty
from lab_python_oop.figure_color import FigureColor


class Figure(ABC):
    def __init__(self):
        self._figure_color = FigureColor()

    def __init__(self, color: FigureColor):
        self._figure_color = color

    def __init__(self, red: int, green: int, blue: int):
        self._figure_color = FigureColor(red, green, blue)

    @abstractmethod
    def area():
        pass

    @property
    def figure_color(self) -> FigureColor:
        return self._figure_color

    @figure_color.setter
    def figure_color(self, color: FigureColor):
        self._figure_color = color

    @figure_color.setter
    def figure_color(self, red: int, green: int, blue: int):
        self._figure_color = FigureColor(red, green, blue)

    @abstractmethod
    def __repr__(self) -> str:
        pass
