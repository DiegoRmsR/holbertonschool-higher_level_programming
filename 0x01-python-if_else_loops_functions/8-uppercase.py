#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        i = ord(str[i])
        if i >= 97 and i <= 122:
            i = i - 32
        print(end="{:c}".format(i))
    print()
