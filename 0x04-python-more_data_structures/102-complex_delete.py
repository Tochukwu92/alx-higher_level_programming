#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_key = list(a_dictionary.keys())
    for va_dic in list_key:
        if value == a_dictionary.get(va_dic):
            del a_dictionary[va_dic]
    return a_dictionary
