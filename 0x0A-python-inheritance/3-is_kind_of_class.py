#!/usr/bin/python3

'''Defines a function.'''


def is_kind_of_class(obj, a_class):
    '''check if obj is istance of a-class or subclass

    Args:
        obj: object to be checked
        a_class: class to be checked
    Return:
        returns True if the object is an instance
    '''
    if isinstance (obj, a_class):
        return True
    else:
        return False
