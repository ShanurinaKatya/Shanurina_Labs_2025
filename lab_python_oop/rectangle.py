from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import FigureColor

class Rectangle(GeometricFigure):
    """Класс Прямоугольник"""

    name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self._color = FigureColor(color)

    #@property
    def color(self):
        return self._color

    def square(self):
        """Вычисление площади прямоугольника"""
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {} площадью {}.".format(
            self.name, self._color.color_property, self.width, self.height, self.square()
        )
