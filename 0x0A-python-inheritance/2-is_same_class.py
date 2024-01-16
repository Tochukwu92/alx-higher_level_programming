#!/usr/bin/python3

'''Checks for an instance.'''


def is_same_class(obj, a_class):
    '''checks if an object is an instance of the class.

    Args:
        obj: the object to be checked
        a_clas: a class to check
    Return:
        returns True if the object is an instance of the class
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
