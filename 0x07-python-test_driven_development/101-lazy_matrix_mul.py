#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    new = np.matmul(m_a, m_b)
    return new
