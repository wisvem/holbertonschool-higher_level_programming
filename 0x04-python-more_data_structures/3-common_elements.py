#!/usr/bin/python3
def common_elements(set_1, set_2):
    ns = set()
    for e1 in set_1:
        for e2 in set_2:
            if e1 == e2:
                ns.add(e1)
                break
    return ns
