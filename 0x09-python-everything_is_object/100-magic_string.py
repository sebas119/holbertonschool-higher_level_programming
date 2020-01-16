#!/usr/bin/python3
def magic_string():
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return ('Holberton, '.__mul__(magic_string.counter - 1) + 'Holberton')
