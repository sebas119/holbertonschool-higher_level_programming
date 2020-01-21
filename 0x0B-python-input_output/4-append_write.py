#!/usr/bin/python3
"""Append text module"""


def append_write(filename="", text=""):
    """Function that appends text at the end of the file"""

    with open(filename, mode='a', encoding="UTF-8") as myfile:
        return myfile.write(text)
