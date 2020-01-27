#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()
    display = "####\n####\n####\n####\n####\n####\n"

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()
    display = "##\n##\n"
