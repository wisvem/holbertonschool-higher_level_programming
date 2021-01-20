#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """MyList class

    Args:
        list (list): list
    """

    def print_sorted(self):
        """print sorted method"""
        nl = self.copy()
        print(sorted(nl))
