#!/usr/bin/python3
"""
function that divides all elements of a matrix.
TypeError: first_name must be a string or last_name must be a string
Return: nothing
"""
def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>
    """
    if type(first_name) !=  str:
        """ first_name must be strings """
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        """ last_name must be strings """
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
