#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for c in range(len(r)):
            print("{}".format(r[c]), end="\n" if len(r)-1 == c else " ")
