#!/usr/bin/python3

import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("{:d} arguments".format(argc), end='')
    if argc == 0:
        print(".")
    else:
        print(":")
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
