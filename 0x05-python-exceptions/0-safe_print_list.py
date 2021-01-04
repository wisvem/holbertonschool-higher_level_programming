#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        l = 0
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            l += 1
        print()
        return l
    except IndexError:
        l = 0
        for i in my_list:
            l += 1
        print()
        return l
