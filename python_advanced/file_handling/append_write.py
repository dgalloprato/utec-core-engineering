#!/usr/bin/env python3
"""Module for appending text to files."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the character count."""
    with open(filename, "a", encoding="utf-8") as archivo:
        return archivo.write(text)
