#!/usr/bin/python3
"""
function that divides all elements of a matrix.
TypeError: matrix must be a matrix (list of lists) of integers/floats
TypeError: Each row of the matrix must have the same size
TypeError: div must be a number
ZeroDivisionError: division by zero
Returns a new matrix
"""

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    i = [[round((element / div), 2) for element in lit_ma]for lit_ma in matrix]

    new_copy = i.copy()

    return new_copy
