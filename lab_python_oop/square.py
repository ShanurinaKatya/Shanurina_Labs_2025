from .rectangle import Rectangle

class Square(Rectangle):
    """Класс Квадрат (наследуется от Прямоугольника)"""

    name = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def color(self):
        return self._color

    def __repr__(self):
        return "{} {} цвета со стороной {} площадью {}.".format(
            self.name, self._color.color_property, self.width, self.square()
        )
