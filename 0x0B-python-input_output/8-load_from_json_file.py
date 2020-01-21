#!/usr/bin/python3

"""Load JSON from a file module"""

import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file"""
    with open(filename, mode='r', encoding="UTF-8") as myfile:

        return json.load(myfile)
