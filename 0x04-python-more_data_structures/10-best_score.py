#!/usr/bin/python3
def best_score(a_dictionary):
    for key in sorted(a_dictionary.keys(), reverse=True):
        return key
    