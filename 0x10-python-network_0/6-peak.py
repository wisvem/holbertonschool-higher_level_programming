#!/usr/bin/python3
"""Generic module"""


def find_peak(list_of_integers):
    """Generic function"""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
