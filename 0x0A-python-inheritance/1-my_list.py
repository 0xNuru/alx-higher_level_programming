#!/usr/bin/python3
"""This module contains a MyList class"""


class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
