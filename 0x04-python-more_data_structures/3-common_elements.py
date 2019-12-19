#!/usr/bin/python3
def common_elements(set_1, set_2):
    inter = []
    if (set_1 and set_2):
        inter = list(set_1.intersection(set_2))
    return inter
