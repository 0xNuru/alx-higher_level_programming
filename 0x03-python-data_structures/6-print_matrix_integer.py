#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:  
        for l in matrix:
            for element in l:
                print("{:d}".format(element), end=" " if element != l[-1] else "")
            print()
