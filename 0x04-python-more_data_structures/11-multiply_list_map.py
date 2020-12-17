#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    cp = []
    cp[:] = map(lambda x: x*number, my_list)
    return cp
