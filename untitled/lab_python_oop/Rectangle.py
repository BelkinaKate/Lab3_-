from lab_python_oop import GeomFigure
from lab_python_oop import Property


class Rectangle(GeomFigure):
    def __init__(self, width, height, color):
        self.__width = width
        self.__height = height
        self.__c = Property.Colour()
        self.__c.col = color
        self.__name = 'Rectangle'

    def square(self):
        return self.__height * self.__height

    def __repr__(self):
        return 'Parameters of figure: \n \
        Width = {} \n \
        Height = {} \n \
        Colour = {} \n \
        Square = {}'.format(self.__width, self.__height, self.__c, self.square())


