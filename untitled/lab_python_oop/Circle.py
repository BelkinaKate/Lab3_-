from lab_python_oop import GeomFigure
from lab_python_oop import Property
import math


class Circle(GeomFigure):
    def __init__(self, radius, color):
        self.__radius = radius
        self.__c = Property.Colour()
        self.__c.col = color
        self.__name = 'Circle'

    def square(self):
        return math.pi * self.__radius ** 2

    def __repr__(self):
        return 'Parameters of figure: \n \
        Radius = {} \n \
        Colour = {} \n \
        Square = {}'.format(self.__radius, self.__c, self.square())
