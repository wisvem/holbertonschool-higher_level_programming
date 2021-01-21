#!/usr/bin/python3
"""Script to add item to a json file"""
import sys

loadjson = __import__('6-load_from_json_file').load_from_json_file
savejson = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
sys.argv.pop(0)
my_list = sys.argv
try:
    my_list = [*loadjson(filename), *my_list]
except Exception:
    pass
savejson(my_list, filename)
