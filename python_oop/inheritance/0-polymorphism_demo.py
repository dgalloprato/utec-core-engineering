#!/usr/bin/env python3
"""Demonstration of inheritance and polymorphism."""


class Animal:
    """Parent class representing an animal."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def speak(self):
        """Return the sound of a dog."""
        return "Woof"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def speak(self):
        """Return the sound of a cat."""
        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
