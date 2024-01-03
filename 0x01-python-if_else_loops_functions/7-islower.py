#!/usr/bin/python3
def islower(c):
    _c = ord(c)
    if _c < ord('a') or _c > ord('z'):
        return True
    else:
        return False
