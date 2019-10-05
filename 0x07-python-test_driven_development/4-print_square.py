#!/usr/bin/python3
"""
function that prints a square with the character #.
TypeError: size must be an integer or size must be >= 0
Return: nothing
"""
def print_square(size):
    """
    prints a square with the character #

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
