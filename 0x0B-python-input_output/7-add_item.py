#!/usr/bin/python3
"""Script to add item to a json file"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
sys.argv.pop(0)
my_list = sys.argv
try:
    my_list = [*load_from_json_file(filename), *my_list]
except Exception:
    pass
save_to_json_file(my_list, filename)
