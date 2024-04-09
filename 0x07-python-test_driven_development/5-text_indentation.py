#!/usr/bin/python3
"""
     a function that prints a text with 2 new lines
     after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        a function that prints a text with 2 new lines
        after each of these characters: ., ? and :
        Args:
            text (str): The text
        Returns:
            None
    """
    if type(text) is not str or text is None or len(text) < 0:
        raise TypeError('text must be a string')

    l = list(text)
    i = 0
    s = len(l)
    while i < s:
        if l[i] == '.' or l[i] == '?' or l[i] == ':':
            if i + 1 != len(l):
                if l[i + 1] == '.' or l[i + 1] == '?' or l[i + 1] == ':':
                    l.insert(i + 1, '\n\n')
                    s +=1
                elif l[i + 1] != ' ':
                    l.insert(i + 1, '\n\n')
                    s += 1
                else:
                    l[i + 1] = '\n\n'
            else:
                l.insert(i + 1, '\n\n')
                s += 1
        i += 1

    x = 0

    while x < s:
        if x + 1 != len(l):
            if l[x] == '\n\n' and l[x + 1] == ' ':
                l.pop(j + 1)
                s -= 1
                continue
        x += 1

    text2 = "".join(l)
    print(text2, end='')
