#!/usr/bin/python3

"""
This is the matrix_mul module and supplies matrix_mul(). For example,
>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]
"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices
    """

    if (not isinstance(m_a, list) or not isinstance(m_a, list)):
        raise TypeError("m_a must be a list or m_b must be a list")

    for el in m_a:
        if (not isinstance(el, list)):
            raise TypeError("m_a must be a list of lists")

    for el in m_b:
        if (not isinstance(el, list)):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for list_el in m_a:
        for el in list_el:
            if (not isinstance(el, (float, int))):
                raise TypeError("m_a should contain only integers or floats")
    for list_el in m_b:
        for el in list_el:
            if (not isinstance(el, (float, int))):
                raise TypeError("m_b should contain only integers or floats")
    row_a = []
    for list_el in m_a:
        row_a.append(len(list_el))
    if (len(set(row_a)) != 1):
        raise TypeError("each row of m_a must be of the same size")
    row_b = []
    for list_el in m_b:
        row_b.append(len(list_el))
    if (len(set(row_b)) != 1):
        raise TypeError("each row of m_b must be of the same size")
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    new = []
    row = []
    ans = 0
    # Number of rows of a
    for i in range(len(m_a)):
        # Number of column of b
        for j in range(len(m_b[0])):
            # Number of rows of b
            for k in range(len(m_b)):
                ans += m_a[i][k] * m_b[k][j]
            row.append(ans)
            ans = 0
        new.append(row)
        row = []
    return new
