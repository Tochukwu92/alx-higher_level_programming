#!/usr/bin/python3
"""
a function that returns the JSON representation of an object (string)
"""
import json
from io import StringIO


def to_json_string(my_obj):
    """
    Converts the given Python object to its JSON representation as a string.
    Parameters:
        my_obj: The Python object to be converted.
    Returns:
        str: The JSON representation of the object as a string.
    """

    json_string = json.dumps(my_obj)
    return json_string
