#!/usr/bin/python3

'''Define a function.'''


def inherits_from(obj, a_class):
    '''Check for instance of an object

    Args:
        obj: object to be checked
        a_class: class to be checked
    Return:
        returns True if the object is an instance of a class
        that inherited (directly or indirectly)
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
