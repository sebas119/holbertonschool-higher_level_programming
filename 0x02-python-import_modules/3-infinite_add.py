#!/usr/bin/python3

import sys

if __name__ == "__main__":
    print(sum(int(sys.argv[i]) for i in range(1, len(sys.argv))))
