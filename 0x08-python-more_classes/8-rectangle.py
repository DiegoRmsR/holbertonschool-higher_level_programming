#!/usr/bin/python3
class Rectangle:
    """ class Rectangle that defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instance method """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return 0
        for i in range(self.__height):
            rectangle += (str(self.print_symbol) * self.__width) + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the object in representation of string """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that delete the object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        instance attribute: bgger_or_equal
        TypeError: rect_1 must be an instance of Rectangle or
        rect_2 must be an instance of Rectangle
        return: rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
