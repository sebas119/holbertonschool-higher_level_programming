#!/usr/bin/python3


def multiple_returns(sentence):

    if len(sentence) == 0:
        firstC = None
    else:
        firstC = sentence[0]
    new = (len(sentence), firstC)
    return new
