#!/usr/bin/python3
import sys
from json import load


loadjson = __import__('6-load_from_json_file').load_from_json_file
savejson = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
sys.argv.pop(0)
my_list = sys.argv
old_list = loadjson(filename)
if old_list is not None:
    savejson((my_list + old_list), filename)
