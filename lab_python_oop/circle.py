import math
from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import FigureColor

class Circle(GeometricFigure):
    """Класс Круг"""

    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self._color = FigureColor(color)

    def color(self):
        return self._color

    def square(self):
        """Вычисление площади круга"""
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "{} {} цвета радиусом {} площадью {}.".format(
            self.name, self._color.color_property, self.radius, self.square()
        )
