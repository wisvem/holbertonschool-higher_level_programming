#!/usr/bin/python3
def no_c(my_string):
    x = my_string.split("c")
    x = "".join(x)
    x = x.split("C")
    x = "".join(x)
    return x
