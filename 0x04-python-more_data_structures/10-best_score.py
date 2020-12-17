#!/usr/bin/python3
def best_score(a_dictionary):
    if(a_dictionary):
        cp = a_dictionary
        for key, value in sorted(cp.items(), key=lambda x: x[1], reverse=True):
            return key
