#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bolea = []
    for num in my_list:
        if num % 2 == 0:
            bolea.append(True)
        else:
            bolea.append(False)
    return bolea
