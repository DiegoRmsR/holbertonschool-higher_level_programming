#!/usr/bin/python3
class Rectangle:
    """ class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ instance method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that returns a value width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        instance attribute: width
        TypeError: width must be an integer
        ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns a value height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        instance attribute: height
        TypeError: height must be an integer
        ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that returns rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Method that returns rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Method that returns a rectangle in # """
        if self.__width == 0 or self.__height == 0:
            return 0
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle
