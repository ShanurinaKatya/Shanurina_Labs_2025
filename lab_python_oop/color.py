class FigureColor:
    """Класс Цвет фигуры"""

    def __init__(self, color):
        self._color = color

    @property
    def color_property(self):
        """Get-аксессор"""
        return self._color

    @color_property.setter
    def color_property(self, value):
        """Set-аксессор"""
        self._color = value
