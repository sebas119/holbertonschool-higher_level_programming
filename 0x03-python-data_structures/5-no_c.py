#!/usr/bin/python3


def no_c(my_string):

    new = "".join([x for x in my_string if x not in ['c', 'C']])
    return new
