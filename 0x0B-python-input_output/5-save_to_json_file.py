#!/usr/bin/python3
"""
a function that writes an Object to a text file, using a JSON representation
"""
import json
from io import StringIO


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to be serialized to JSON.
        filename (str): The name of the file to save the JSON data
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(my_obj, f)
