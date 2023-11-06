#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:  
        for l in matrix:
            for element in l:
                print("{:d}".format(element), end=" ")
            print()
