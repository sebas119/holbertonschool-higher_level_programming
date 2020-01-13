#!/usr/bin/python3


def text_indentation(text):

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    text = text.replace(':', ':*&*').replace('?',
                                             '?*&*').replace('.', '.*&*')
    text = text.split('*&*')

    new = []
    for el in text:
        new.append(el.strip())
    for val in new:
        if (val[-1] in {':', '?', '.'}):
            print(val, end='\n\n')
        else:
            print(val, end='')
