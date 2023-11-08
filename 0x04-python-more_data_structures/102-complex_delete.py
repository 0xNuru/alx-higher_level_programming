#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    list_view = a_dictionary.keys()
    list_keys = list(list_view)

    for value in list_keys:
        if value == a_dictionary.get(value):
            del a_dictionary[value]

    return (a_dictionary)
