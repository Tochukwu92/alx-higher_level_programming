#!/usr/bin/python3
'''Define a class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Introduce a class Rectangle that inherits from BaseGeometry.'''

    def __init__(self, width, height):
        '''Initialize the classs.
        
        Args:
            width: the width of the object
            height: the height of the object
        '''
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        '''calculates the area of a rectangle.

        Return:
            returns the area of the rectangle.
        '''
        return (self.__width * self.__height)
    def __str__(self):
        '''print the object.

        Return:
            returns the object.
        '''
        return f"{[Rectangle]} {self.__width}/{self.__height}"
