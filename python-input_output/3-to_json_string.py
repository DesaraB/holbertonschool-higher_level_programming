#!/usr/bin/python3
import json


"""Module that returns the JSON representation of an obj str"""


def to_json_string(my_obj):
    """func that converts obj to json str"""
    return json.dumps(my_obj)
