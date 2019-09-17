#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i == 'C' or i == 'c':
            my_string = my_string.translate({ord(i): None})
    return my_string
