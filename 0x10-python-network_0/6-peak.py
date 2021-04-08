#!/usr/bin/python3
"""Generic module"""


def find_peak(list_of_integers):
    """Generic function"""
    list_len = len(list_of_integers)
    if (list_len is 0):
        return None
    x = list_of_integers[0]
    for i in range(int(list_len/2)):
        if (x < list_of_integers[0]):
            x = list_of_integers[0]
        if (x < list_of_integers[list_len - 1 - i]):
            x = list_of_integers[list_len - 1 - i]
    return x
