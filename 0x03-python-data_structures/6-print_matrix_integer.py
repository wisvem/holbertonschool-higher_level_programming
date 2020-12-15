#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for r in matrix:
            if len(r) == 0:
                print()
            for c in range(len(r)):
                print("{:d}".format(r[c]), end="\n" if len(r)-1 == c else " ")
