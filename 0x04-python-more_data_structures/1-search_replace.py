#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nl = my_list.copy()
    for i in range(len(nl)):
        if (nl[i] == search):
            nl[i] = replace
    return nl
