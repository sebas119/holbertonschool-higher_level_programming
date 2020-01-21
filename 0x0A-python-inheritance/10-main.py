#!/usr/bin/python3
Square = __import__('10-square').Square
Rectangle = __import__('9-rectangle').Rectangle

s = Square(13)

print(s)
print(s.area())
print(issubclass(Square, Rectangle))
