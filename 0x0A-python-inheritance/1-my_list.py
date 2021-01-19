#!/usr/bin/python3
"""[summary]
    """


class MyList(list):
    """[summary]

    Args:
        list ([type]): [description]
    """

    def __init__(self):
        pass

    def print_sorted(self):
        """[summary]
        """
        nl = self.copy()
        print(sorted(nl))
