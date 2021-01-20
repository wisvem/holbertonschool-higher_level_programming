#!/usr/bin/python3
"""FIle open module"""


def read_file(file):
    """Open file function

    Args:
        file (file): file to be opened
    """
    with open(file, "r", encoding="utf-8") as f:
        print(f.read().decode())
