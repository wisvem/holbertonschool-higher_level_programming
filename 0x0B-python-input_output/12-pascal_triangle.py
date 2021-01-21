#!/usr/bin/python3
"""pascal traingle module"""


def pascal_triangle(n):
    """pascal triangle function

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    triangle = [[1], [1, 1]]
    for i in range(1, n):
        floor = [1]
        for j in range(0, len(triangle[i])-1):
            floor.extend([triangle[i][j] + triangle[i][j+1]])
        floor += [1]
        triangle.append(floor)
    return triangle
