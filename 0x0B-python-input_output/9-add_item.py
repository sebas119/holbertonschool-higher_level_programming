#!/usr/bin/python3

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

args = sys.argv[1:]
try:
    myJson = load_from_json_file(filename)
    if myJson is None:
        myJson = []
except Exception:
    myJson = []

if myJson == [] and len(sys.argv) == 1:
    save_to_json_file(myJson, filename)
else:
    for el in args:
        myJson.append(el)
    save_to_json_file(myJson, filename)
