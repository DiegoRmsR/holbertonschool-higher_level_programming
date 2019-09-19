#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if (length == 0):
        return (None)
    num_max = 0
    for i in range(len(my_list)):
        if num_max < my_list[i]:
            num_max = my_list[i]
    return num_max
