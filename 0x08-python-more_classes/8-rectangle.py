#!/usr/bin/python3
"""
    A module that create a class Rectangle
"""


class Rectangle:
    """
       A class that create an instance of a Rectangle:
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializing a rectangle with width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """return area of our rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of our rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Print our rectangle"""
        if self.perimeter() == 0:
            return ""
        else:
            return "\n".join([
                str(self.print_symbol) * self.width
                for i in range(0, self.height)
            ])

    def __repr__(self):
        """Return string representation of our rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Find biggest Rectangle"""
        if not(isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not(isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.perimeter() > rect_2.perimeter():
            return rect_1
        elif rect_2.perimeter() > rect_1.perimeter():
            return rect_2
        else:
            return rect_1

    def __del__(self):
        """Here is the obj destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
