#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add functions
    Args:
        a (int) || (float): First args
        b (int) || (float): Second args
    Returns:
        int: a + b
    """
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not(isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
