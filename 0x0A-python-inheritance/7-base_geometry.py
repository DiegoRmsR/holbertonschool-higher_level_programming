#!/usr/bin/python3
class BaseGeometry:
    """
    class
    """
    def area(self):
        """
        instance method area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        instance method that validates value

        TypeError: <name> must be an integer
        ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
