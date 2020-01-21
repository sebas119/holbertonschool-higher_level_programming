#!/usr/bin/python3
"""Write line module"""


def write_file(filename="", text=""):
    """Function that write lines in a file"""

    with open(filename, mode='w', encoding="UTF-8") as myfile:

        return myfile.write(text)
