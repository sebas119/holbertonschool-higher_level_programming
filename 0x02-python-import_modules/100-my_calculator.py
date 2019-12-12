#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    import sys
    if (len(sys.argv) != 4):
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if (op not in ['+', '-', '*', '/']):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if (op is '+'):
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif (op is '-'):
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif (op is '*'):
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
