#!/usr/bin/python3

"""
This is the integers addition module and supplies add_integer(). For example,
>>> factorial(5)
120
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers
    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    else:
        if (isinstance(a, float)):
            a = int(a)
        if (isinstance(b, float)):
            b = int(b)
        return a + b
