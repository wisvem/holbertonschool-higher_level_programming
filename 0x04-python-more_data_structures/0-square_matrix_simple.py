#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda x : x * x
    matrix2 = list(map(list, matrix))
    for r in matrix2:
        for c in range(len(r)):
            r[c] = square(r[c])
    return matrix2
