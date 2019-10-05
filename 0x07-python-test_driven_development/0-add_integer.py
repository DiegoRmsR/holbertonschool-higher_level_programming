#!/usr/bin/python3
"""
function that adds 2 integers.
TypeError: a must be an integer or b must be an integer
Return: nothing
"""
def add_integer(a, b=98):
    """
    Add 2 integers
    """
    if isinstance(a, float):
        """ cast a if is float """
        a = int(a)
    if isinstance(b, float):
        """ cast b if is float """
        b = int(b)

    if not isinstance(a, int):
        """ a must be an integer """
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        """ b must be an integer """
        raise TypeError("b must be an integer")
    return a + b
