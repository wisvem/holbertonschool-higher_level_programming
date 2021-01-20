#!/usr/bin/python3
"""Module"""


class MyInt(int):
    """Class"""

    def __ini__(self, value):
        super().__init__()

    def __eq__(self, other):
        """Equal method"""
        return int(self) != other

    def __ne__(self, other):
        """Not equal method"""
        return int(self) == other
