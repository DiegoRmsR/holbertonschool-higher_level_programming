#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    for list_reverse in reversed(my_list):
        str = "{:d}"
        print(str.format(list_reverse))
