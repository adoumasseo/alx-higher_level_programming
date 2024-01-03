#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= i <= ord('z'):
            print("{:c}".format({char(ord(i) + 32)), end='')
        else:
        print("{:c}".format(i), end='')
