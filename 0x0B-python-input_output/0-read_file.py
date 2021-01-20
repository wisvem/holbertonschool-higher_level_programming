#!/usr/bin/python3
"""filename open module"""


def read_file(filename=""):
    """read file function

    Args:
        filename (str, optional): [description]. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read().decode())
