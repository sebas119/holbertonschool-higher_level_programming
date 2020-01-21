#!/usr/bin/python3

"""String to JSON module"""

import json


def from_json_string(my_str):
    """Function that returns a object represented by a JSON string"""
    return json.loads(my_str)
