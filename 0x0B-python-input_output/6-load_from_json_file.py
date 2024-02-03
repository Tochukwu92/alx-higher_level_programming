#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file
"""

import json
from io import StringIO

def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.
    Returns:
        dict, list, or set: The Python object created from the JSON data
    """

    with open(filename, 'r', encoding="UTF-8") as f:
       data =  json.load(f)
    return data
