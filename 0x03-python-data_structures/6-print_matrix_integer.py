#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            print("{}".format(row[col]), end="\n" if len(row)-1 == col else " ")
