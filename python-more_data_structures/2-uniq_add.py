#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    result = 0
    for elem in new_list:
        result += elem
    return result
