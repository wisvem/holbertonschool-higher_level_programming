#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """MyList class

    Args:
        list (list): list
    """

    def __init__(self):
        pass

    def print_sorted(self):
        """print sorted method"""
        nl = self.copy()
        print(sorted(nl))
