from abc import ABC, abstractmethod
from lab_python_oop.color import FigureColor

class GeometricFigure(ABC):
    """Абстрактный класс Геометрическая фигура"""

    @abstractmethod
    def square(self):
        """Абстрактный метод для вычисления площади"""
        pass

    @abstractmethod
    def name(self):
        """Абстрактное свойство для названия фигуры"""
        pass

    @abstractmethod
    def color(self):
        """Абстрактное свойство для доступа к цвету"""
        pass

    @abstractmethod
    def __repr__(self):
        """Строковое представление фигуры"""
        return "{} {} цвета площадью {:.2f}".format(
            self.name,
            self.color(),
            self.square()
        )
