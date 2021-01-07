#!/usr/bin/python3
"""Module to add integers"""


def add_integer(a, b=98):
    """Add two int or float

    Args:
        a (int: first integer]
        b (int, optional): second integer. Defaults to 98.

    Raises:
        TypeError: whether a or b don't match type int or float

    Returns:
        int: a and b addition
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a)+int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
