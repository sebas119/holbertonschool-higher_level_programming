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
    flag = False
    for c in text:

        if (flag is True and c is ' '):
            continue
        flag = False
        if (c in {'.', ':', '?'}):
            print(c, end="\n\n")
            flag = True
        else:
            print(c, end='')
