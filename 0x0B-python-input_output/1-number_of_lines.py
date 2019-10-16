#!/usr/bin/python3
"""
function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        num_lines = 0
        for lines in f:
            num_lines += 1
    return num_lines
