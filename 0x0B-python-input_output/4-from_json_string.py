#!/usr/bin/python3
"""
a function that returns an object (Python data structure)
represented by a JSON string
"""
import json
from io import StringIO


def from_json_string(my_str):
    """
    Convert a JSON string into a Python object.
    Parameters:
    - json_string (str): A JSON-formatted string.
    Returns:
    - dict or list: The Python object representing the JSON data.
    Raises:
    - json.JSONDecodeError: If the input string is not valid JSON.
    """

    content = json.loads(my_str)
    return content
