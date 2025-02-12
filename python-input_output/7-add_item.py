#!/usr/bin/python3

"""
This module provides a a script that adds all
arguments to a Python list, and then save them to a file:
"""

import os
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

the_list = []
if os.path.exists("add_item.json"):
    the_list = load_from_json_file("add_item.json")
for i in range(1, len(argv)):
    the_list.append(argv[n])
save_to_json_file(the_list, "add_item.json")
