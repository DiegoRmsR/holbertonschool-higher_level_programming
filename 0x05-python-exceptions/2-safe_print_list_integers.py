#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print(end="{:d}".format(my_list[i]))
            num += 1
        except(TypeError, ValueError):
            pass
    print()
    return(num)
