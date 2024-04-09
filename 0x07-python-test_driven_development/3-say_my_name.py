#!/usr/bin/python3
"""
     a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
        a function that prints My name is <first name> <last name>
        Args:
            first_name (string): as his name :)
            last_name (string): as his name :) :)
        Returns:
            None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
