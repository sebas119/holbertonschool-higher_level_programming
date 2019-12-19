#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    keyDict = a_dictionary.keys()

    if (key in keyDict):
        del a_dictionary[key]
    return a_dictionary
