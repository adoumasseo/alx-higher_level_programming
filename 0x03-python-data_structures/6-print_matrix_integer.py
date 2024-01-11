#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for j in range(0, len(i)):
                sep = " "
                if j == len(i) - 1:
                    sep = ""
                print("{:d}".format(i[j]), end=sep)
            print()
