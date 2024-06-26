#!/usr/bin/python3
"""
    A module that create a class Rectangle
"""


class Rectangle:
    """
       A class that create an instance of a Rectangle:
    """
    def __init__(self, width=0, height=0):
        """ Initializing a rectangle with width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ A getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ A setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ A getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ A setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
