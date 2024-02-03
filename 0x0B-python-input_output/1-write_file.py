#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    Writes the given text to the specified file in UTF-8 encoding.
    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.
    Returns:
        int: The number of characters written to the file.
    """

    with open("filename", 'w', encoding='UTF8') as f:
        content = f.write(text)
        return content
