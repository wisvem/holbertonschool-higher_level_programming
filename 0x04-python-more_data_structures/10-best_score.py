#!/usr/bin/python3
def best_score(a_dictionary):
    if(a_dictionary):
        for key in sorted(a_dictionary.values(), reverse=True):
            return key
