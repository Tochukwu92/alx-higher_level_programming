#!/usr/bin/python3

def add_integer(a, b=98):
    '''Add two integers

    Args:
        a (int): first parameter
        b (int): second parameter
    Return: a + b
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
