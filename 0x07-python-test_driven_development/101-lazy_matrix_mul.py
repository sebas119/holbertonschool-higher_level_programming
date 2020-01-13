#!/usr/bin/python3
import numpy as np

"""
This is the lazy_matrix_mul module and supplies lazy_matrix_mul(). For example,
>>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices with numpy module
    """

    new = np.matmul(m_a, m_b)
    return new
