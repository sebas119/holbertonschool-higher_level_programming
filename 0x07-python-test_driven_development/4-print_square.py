#!/usr/bin/python3

"""
This is the print_square module and supplies print_square(). For example,
>>> print_square(1)
#
"""


def print_square(size):
    """
    Function that prints a square with the character #
    """

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise TypeError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
