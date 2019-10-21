#!/usr/bin/python3
""" class Base """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method that return the area of the rectangle object """
        return self.__width * self.__height

    def display(self):
        """ Method that prints in stdout the Rectangle
        instance with the character # """
        for v in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """ Method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        argm = "({}) {}/{} - ".format(self.id, self.x, self.y)
        argm += "{}/{}".format(self.width, self.height)
        return "[Rectangle] " + argm

    def update(self, *args, **kwargs):
        if len(args) != 0 and args:
            l_attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, l_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
