#!/usr/bin/python3
'''Square module'''


class Square:
    '''A class with something'''
    def __init__(self, size = 0):
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
