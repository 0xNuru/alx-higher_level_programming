#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        highest = 0
        for element in my_list:
            if element > highest:
                highest = element

        return highest
