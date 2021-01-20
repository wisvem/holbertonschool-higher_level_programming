#!/usr/bin/python3
"""write in a file module"""


def write_file(filename="", text=""):
    """FUnction to write in a file

    Args:
        filename (str, optional): path to file. Defaults to "".
        text (str, optional): characters to write. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
