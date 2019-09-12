#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    if num == 0:
        print("{:d} arguments.".format(num))
    elif num == 1:
        print("{:d} argument:".format(num))
    else:
        print("{:d} arguments:".format(num))
    if num > 0:
        num = 1
        for arg in sys.argv[1:]:
            print("{:d}: {}".format(num, arg))
            num += 1
