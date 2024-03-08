def my_function(a, times):
    """A fct to mutltipy
    Work with string

    >>> my_function('a', 3)
    'aaa'

    and number
    >>> my_function(9, 3) #doctest: +NORMALIZE_WHITESPACE
    27       


    not with two string

    >>> my_function('a', 'b')
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/home/ortniel/alxproject/alx-higher_level_programming/test.py", line 2, in my_function
        return a * times
    TypeError: can't multiply sequence by non-int of type 'str'
    """
    return a * times
class My_class:
    pass

def unpredicable(obj):
    """
    Unpredicable test
    >>> unpredicable(My_class()) #doctest: +ELLIPSIS
    [<test.My_class object at 0x...>]
    """
    return [obj]
