#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (i != 8 or j != 9):
            if (i != j and i < j):
                print("{:d}{:d}, ".format(i, j), end="",)
        elif (i == 8 and j == 9):
            print("{:d}{:d}".format(i, j))
