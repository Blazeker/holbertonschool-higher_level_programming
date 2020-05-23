#!/usr/bin/python3
""" Divide the matrix """


def matrix_divided(matrix, div):
    """ Divide the matrix with the div variable """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    lenR = -1
    newM = []
    msj1 = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if (lenR != len(row) and lenR != -1):
            raise TypeError("Each row of the matrix must have the same size")
        newL = []
        for j in row:
            if type(j) is not int and type(j) is not float:
                raise TypeError(msj1)
                return matrix
            else:
                newL.append(round(j / div, 2))
        newM.append(newL)
        lenR = len(row)
    return newM
