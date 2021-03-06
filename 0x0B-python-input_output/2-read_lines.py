#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):

    with open(filename, mode="r", encoding="UTF-8") as myfile:

        if nb_lines <= 0 or nb_lines >= sum(1 for line in myfile):
            myfile.seek(0)
            print(myfile.read(), end='')
        else:
            myfile.seek(0)
            for i in range(nb_lines):
                print(myfile.readline(), end='')
