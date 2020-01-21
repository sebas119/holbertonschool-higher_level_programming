#!/usr/bin/python3


def number_of_lines(filename=""):

    with open(filename, mode="r", encoding="UTF-8") as myfile:
        return len(myfile.readlines())
