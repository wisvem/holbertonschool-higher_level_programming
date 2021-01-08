#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """print a graphical representation of square
    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not int or less than 0
        ValueError: 
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size > 0:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
    elif size == 0:
        pass
    else:
        raise ValueError("size must be >= 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
