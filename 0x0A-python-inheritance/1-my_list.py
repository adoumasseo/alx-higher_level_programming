#!/usr/bin/python3
"""
A module that define a class inherit of list & define a sorte method inside
"""


class MyList(list):
    """ A class that inherit from list"""
    def __init__(self):
        """Init fonction"""
        super().__init__()

    def print_sorted(self):
        """ A fct two sort a list"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
