#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    new = []
    if not my_list:
        return new
    for elem in my_list:
        if elem % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
