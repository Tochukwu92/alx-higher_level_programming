#!/usr/bin/python3

'''Define a square. '''


class Square:
    '''Represent a new square. '''

    def __init__(self, size=0):
        '''Initialize the square.

        Args:
            size (int): the size of the square

        '''
        self.size = size

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

    def area(self):
        '''Returns the current area of the square '''
        return (self.__size * self.__size)

    def my_print(self):
        '''Print a square with # character. '''
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("")
