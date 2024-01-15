#!/usr/bin/python3

def matrix_divided(matrix, div):
    '''Divides a matrix with a scala.

    Args:
        matrix (int): a list of lists to be divided
        div (int): integer used to divide the matrix
    Return:
        a new matrix showing the result of th division
    '''
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in matrix for num in row])):
         raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append((round(matrix[i][j] / div, 2)))
        new_matrix.append(new_row)
    return new_matrix
