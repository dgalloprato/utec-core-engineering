#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado con tamaño privdo."""

    def __init__(self, size=0):
        """Inicializa el tamaño del cuadrado."""
        self.size = size

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y establece el tamaño del cuadrado."""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2
