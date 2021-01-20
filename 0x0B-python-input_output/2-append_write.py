#!/usr/bin/python3
"""Module to append"""


def append_write(filename="", text=""):
    """Function to append text

    Args:
        filename (str, optional): filepath . Defaults to "".
        text (str, optional): characters. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
