#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado con tamaño y posición."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el tamaño y la posición del cuadrado."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Devuelve la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y establece la posición del cuadrado."""
        if (type(value) is not tuple or len(value) != 2
                or type(value[0]) is not int
                or type(value[1]) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integer"
            )

        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con su posición."""
        print(self.__str__())

    def __str__(self):
        """Devuelve el cuadrado como una cadena."""
        if self.__size == 0:
            return ""

        square = "\n" * self.__position[1]

        for i in range(self.__size):
            square += " " * self.__position[0]
            square += "#" * self.__size

            if i < self.__size - 1:
                square += "\n"

        return square
