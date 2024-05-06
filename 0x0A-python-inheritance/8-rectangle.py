#!/usr/bin/python3
"""
    A module for an Geometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Geometry Class
    """
    def __init__(self, width, height):
        """Init fonction"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
