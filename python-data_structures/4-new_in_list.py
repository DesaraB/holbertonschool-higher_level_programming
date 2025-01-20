#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_in_list = my_list.copy()

    if idx < 0:
        return new_in_list
    if idx >= len(my_list):
        return new_in_list
    new_list = new_in_list
    new_list[idx] = element
    return new_in_list
