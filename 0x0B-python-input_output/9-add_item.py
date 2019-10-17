#!/usr/bin/python3
"""
script that adds all arguments to a Python
list, and then save them to a file
"""


from sys import argv
import os

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

list = []
if os.path.exists("add_item.json"):
    list = load_from_json_file("add_item.json")

for i in argv[1:]:
    list.append(i)
save_to_json_file(list, "add_item.json")
