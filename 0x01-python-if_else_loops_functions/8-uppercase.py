#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= i <= ord('z'):
            print(f"{char(ord(i) + 32)}")
        else:
            print(f"{i}")
