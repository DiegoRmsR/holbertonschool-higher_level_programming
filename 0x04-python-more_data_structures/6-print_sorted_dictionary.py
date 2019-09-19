#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictionary = sorted(a_dictionary.keys())
    for i in dictionary:
        print("{}: {}".format(i, a_dictionary.get(i)))
