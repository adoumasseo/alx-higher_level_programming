#!/usr/bin/python3
"""
     a function that prints a square with the character #.
"""


def print_square(size):
    """
        a function that prints a square with the character #.
        Args:
            size (int): size of our square
        Returns:
            None
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print('')
