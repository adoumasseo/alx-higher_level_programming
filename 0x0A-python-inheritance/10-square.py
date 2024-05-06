#!/usr/bin/python3
"""
    A module for an Geometry class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Geometry Class
    """
    def __init__(self, size):
        """Init fonction"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Compute the area"""
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
