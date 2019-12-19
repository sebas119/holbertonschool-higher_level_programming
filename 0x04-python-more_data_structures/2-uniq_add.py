#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = 0
    if my_list:
        new = sum(list(set(my_list.copy())))
    return new
