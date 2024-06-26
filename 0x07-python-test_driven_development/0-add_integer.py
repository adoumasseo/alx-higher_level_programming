#!/usr/bin/python3
"""
This module contains functions for adding two integer
"""


def add_integer(a, b=98):
    """
    This function compute sum of two numbers
    Args:
        a (int or float): First args
        b (int or float): Second args default 98
    Returns:
        int: a + b
    """
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not(isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
