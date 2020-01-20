#!/usr/bin/python3


class MyInt(int):

    def __eq__(self, value):
        if (self.real == value):
            return False
        return True

    def __ne__(self, value):
        if (self.real != value):
            return False
        return True
