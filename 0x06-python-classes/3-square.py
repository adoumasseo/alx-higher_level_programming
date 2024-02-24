#!/usr/bin/python3
"""A class that create a square"""


class Square:
    """
    A class that create a square
    Attributes:
        size (int): The size of our square, size >= 0
    """

    def __init__(self, size=0):
        """Initializing the class
        Args:
            size (int): The size of our square, size >= 0
        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """
        A method to get value of size
        Args:
            None
        Returns:
            int: Size of our square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Seting and checking value of size
        Args:
            size (int): The size of our square, size >= 0
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """Return Area of square
        Args:
            None
        Returns:
            int: Area of square
        """
        return (self.__size * self.__size)
