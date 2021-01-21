#!/usr/bin/python3
"""This module defines a function"""


def pascal_triangle(n):
    """Pascal triangel function"""
    results = []
    for _ in range(n):
        row = [1]
        if results:
            last_row = results[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        results.append(row)
    return results
