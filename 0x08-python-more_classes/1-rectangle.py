#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""
class Rectangle:
    """  """
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
