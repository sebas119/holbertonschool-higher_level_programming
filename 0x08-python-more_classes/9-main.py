#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)


my_square = Rectangle.square(10)
print("{} / {}".format(my_square.width, my_square.height))
