#!/usr/bin/python
"""
function that reads n lines of a text file (UTF8)
"""


def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding="utf-8") as f:
        if nb_lines <= 0:
            read_date = f.read()
            print(read_date, end='')
        else:
            for n_lines in range(nb_lines):
                read_line = f.readline()
                print(read_line, end='')
