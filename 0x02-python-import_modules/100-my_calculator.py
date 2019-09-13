#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    inarg = len(sys.argv) - 1
    if inarg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>T")
        sys.exit(1)

    ope = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if ope == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif ope == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif ope == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    elif ope == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)
