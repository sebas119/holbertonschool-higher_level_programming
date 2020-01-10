#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) is False or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(val) != int for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(val < 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
