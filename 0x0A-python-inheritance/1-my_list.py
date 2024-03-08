#!/usr/bin/python3
"""
A module that define a class inherit from list & define a sorte method inside
"""


class MyList(list):
    """ A class that inherit from list"""
    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print(new_list)
