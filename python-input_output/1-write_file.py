#!/usr/bin/python3


"""Module that contains the function write_file."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the nr of char"""
    with open(filename, "w", encoding="UTF8") as f:
        content = f.write(text)
        return content
