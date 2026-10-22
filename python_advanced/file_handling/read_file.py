#!/usr/bin/env python3
"""Module for reading text files."""


def read_file(filename=""):
    """Read and print the contents of a UTF-8 text file."""
    with open(filename, encoding="utf-8") as archivo:
        print(archivo.read(), end="")
