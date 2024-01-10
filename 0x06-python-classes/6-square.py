#!/usr/bin/python3

'''Define a square. '''


class Square:
    '''Represent a new square. '''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize the square.

        Args:
            size (int): the size of the square

        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Get/set the current sie of the square. '''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Get/set current position of the square. '''
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or 
                not all(isinstance(n, int) for n in value)
                or not all(n > 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Returns the current area of the square '''
        return (self.__size * self.__size)

    def my_print(self):
        '''Print a square with # character. '''
        if self.__size == 0:
            print("")
            return
