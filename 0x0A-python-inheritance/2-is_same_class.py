#!/usr/bin/python3
def is_same_class(obj, a_class):

    if isinstance(obj, a_class) is True and type(obj) == a_class:
        return True
    return False
