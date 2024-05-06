#!/usr/bin/python3
"""
    How to check if an class is an subclass of an other one.
"""


def inherits_from(obj, a_class):
    """
        Check if obj is instance of a class that inherited of a_class

        Args:
            obj (any): the object to check
            a_class (any): The Baseclass
        Returns:
            True: if the object is an instance of a class that inherited
            False: otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
