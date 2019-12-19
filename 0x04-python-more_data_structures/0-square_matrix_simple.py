#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixNew = []
    if matrix:
        for row in matrix:
            rowlist = []
            for val in row:
                rowlist.append(val**2)
            matrixNew.append(rowlist)
    return matrixNew
