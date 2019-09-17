#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx < 0 and idx > i:
            return none
    return my_list[idx]
