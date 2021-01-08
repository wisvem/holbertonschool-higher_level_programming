#!/usr/bin/python3
"""Say my name nmodule"""


def say_my_name(first_name, last_name=""):
    """function to print full name

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: first_name or last_name not a string
    """
    m1 = "must be a string"
    if type(first_name) is not str:
        raise TypeError("first_name {}".format(m1))
    if type(last_name) is not str:
        raise TypeError("last_name {}".format(m1))
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
