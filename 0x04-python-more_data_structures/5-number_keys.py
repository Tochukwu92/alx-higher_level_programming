#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    dic_keys = list(a_dictionary.keys())
    for key in dic_keys:
        count = count + 1
    return count
