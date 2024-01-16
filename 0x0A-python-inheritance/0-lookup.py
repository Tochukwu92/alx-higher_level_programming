#!/usr/bin/python3

def lookup(obj):
    '''Finds the attribute and method of an object

    Args:
        obj: parameter pass the function
    Return:
         returns the list of available attributes and methods of an objec
    '''
    return dir(obj)
