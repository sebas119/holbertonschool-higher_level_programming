#!/usr/bin/python3

"""
This is the 2-matrix_divided module and supplies matrix_divided(). For example,
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    matrixExMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list)):
        raise TypeError(matrixExMsg)
    size = []
    for el in matrix:
        if (not isinstance(el, list) or len(el) == 0):
            raise TypeError(matrixExMsg)
        size.append(len(el))
        for data in el:
            if (not isinstance(data, (int, float))):
                raise TypeError(matrixExMsg)
    if (len(set(size)) != 1):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")

    new = []
    inter = []
    for el in matrix:
        for data in el:
            inter.append(round(data/div, 2))
        new.append(inter)
        inter = []
    return new
