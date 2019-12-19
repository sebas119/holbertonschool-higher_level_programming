#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    if my_list:
        for val in my_list:
            if (val == search):
                val = replace
            new.append(val)
    return new
