#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = list(map(list, matrix))
    for r in matrix2:
        for c in range(len(r)):
            r[c] = r[c]*r[c]
    return matrix2
