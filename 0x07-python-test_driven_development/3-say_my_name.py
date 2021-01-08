#!/usr/bin/python3
"""Say my name nmodule"""


def say_my_name(first_name, last_name=""):
    """[summary]

    Args:
        first_name ([type]): [description]
        last_name (str, optional): [description]. Defaults to "".

    Raises:
        TypeError: [description]
        TypeError: [description]
    """
    m1 = "must be a string"
    if type(first_name) is not str:
        raise TypeError("first_name {}".format(m1))
    if type(last_name) is not str:
        raise TypeError("last_name {}".format(m1))
    print("My name is {} {}".format(first_name, last_name))
