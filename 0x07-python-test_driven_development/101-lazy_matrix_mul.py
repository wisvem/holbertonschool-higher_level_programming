#!/usr/bin/python3
"""lazy matrix module"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    a = np.array(m_a)
    b = np.array(m_b)
    res = np.dot(a, b)
    return res
