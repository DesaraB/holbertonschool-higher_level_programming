#!/usr/bin/python3


"""Module that contains the function append_write."""


def append_write(filename="", text=""):
    """Writes a string to a text file (UTF8)"""
    with open(filename, "a", encoding="UTF8") as f:
        content = f.write(text)
        return content
