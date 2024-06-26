#!/usr/bin/python3
"""
    A module for an Geometry class
"""


class BaseGeometry:
    """
        Geometry Class
    """
    def area(self):
        """
            A fct to calcul area of a Geomotry figure
            Args:
                self: An instance of BaseGeometry
            Returns:
                Just Raise an Exception for now
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Purpose is to validate value
            Args:
                self: an instance of BaseGeometry
                name (string): Name of our value
                value (int): value must be int
            Returns:
                Nothing just Validate value
                and raise specific exception if sometimes gone wrong
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
