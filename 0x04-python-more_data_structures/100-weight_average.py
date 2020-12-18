#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    if my_list:
        resi = 1
        resx = 0
        for e in my_list:
            resi = 1
            for t in e:
                resi = resi*t
            resx = resx + t
            res = res+resi
        res = res/resx
    return res
