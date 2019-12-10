#!/usr/bin/python3
for i in range(ord('z'), ord('`'), -1):
    if (i % 2 == 0):
        print("{:c}".format(i), end='')
    else:
        print("{:c}".format(i - ord(' ')), end='')
