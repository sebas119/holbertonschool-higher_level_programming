#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ans = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        ans = None
    return ans
