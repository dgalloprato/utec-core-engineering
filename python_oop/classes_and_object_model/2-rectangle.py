#!/usr/bin/env python3
"""Módulo que define la clase Rectangle."""


class Rectangle:
    """Representa un rectángulo."""

    def __init__(self, width=0, height=0):
        """Inicializa el ancho y el alto."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Devuelve el ancho."""
        return self.__width

    @width.setter
    def width(self, value):
        """Valida y establece el ancho."""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Devuelve el alto."""
        return self.__height

    @height.setter
    def height(self, value):
        """Valida y establece el alto."""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Devuelve el perímetro del rectángulo."""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
