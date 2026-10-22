#!/usr/bin/env python3
"""Module for writing text to files."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the character count."""
    with open(filename, "w", encoding="utf-8") as archivo:
        return archivo.write(text)
