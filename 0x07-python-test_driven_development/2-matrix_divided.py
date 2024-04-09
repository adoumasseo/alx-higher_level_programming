#!/usr/bin/python3
"""
This module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix
    Args:
        matrix (list): a list of lists of int and float
        div (int or float): a number to divides each elt of matrix
    Returns:
        list: a new list with result of number divide
    """
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        else:
            lenlist = len(lists)
            for item in lists:
                if type(item) is not int and type(item) is not float:
                    raise TypeError("matrix must be a matrix" +
                                    "(list of lists) of integers/floats")
    for lists in matrix:
        if len(lists) != lenlist:
            raise TypeError("Each row of the matrix must have the same size")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    else:
        return [[round(item / div, 2) for item in lists] for lists in matrix]
