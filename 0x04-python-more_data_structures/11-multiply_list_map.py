#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    cp = my_list.copy()
    cp[:] = map(lambda x: x*number, cp)
    return cp
