#!/usr/bin/python3
def element_at(my_list, idx):
    i = len(my_list)
    if idx < 0 or idx > i - 1:
        return None
    return my_list[idx]
