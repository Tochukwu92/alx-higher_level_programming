#!/usr/bin/python3

'''Define a class Square. '''


class Square:
    '''Represent a new square. '''

    def __init__(self, size=0):
        '''Initialize the square.

        Args:
            size (int): the size of the square

        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        '''Returns the current area of the square '''
        return self.size * self.size
