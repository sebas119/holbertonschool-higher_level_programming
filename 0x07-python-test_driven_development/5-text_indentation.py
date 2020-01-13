#!/usr/bin/python3

"""
This is the text_indentation module and supplies text_indentation().
For example,
>>> text_indentation(text)
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after (., :, ?)
    """

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
