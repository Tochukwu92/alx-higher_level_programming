#!/usr/bin/python3

'''Define a class.'''


class BaseGeometry:
    '''Introduce a class BaseGeometry.'''

    def area(self):
        '''Define a function area.'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Function that validates the parameters.

        Args:
            name: assumed to be always a string
            value: parameter to be validated
        Return:
            returns a validated value
        '''
        if not isinstance(value, int):
            raise TypeError(str(self.value) + " must be an integer")
        if value <= 0:
            raise ValueError(str(self.value) + " must be greater than 0")
        self.name = name
        self.value = value

