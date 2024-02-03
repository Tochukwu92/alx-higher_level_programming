#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Opens a text file and prints its content to the standard output.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        store = f.read()
        print(store)
