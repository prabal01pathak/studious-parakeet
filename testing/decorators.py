#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
a decorator is a function that takes another function and 
extends the behavior of the latter function without explicitly modifying it
'''

def convert_upper(f):
    print("convert_upper")
    def wrap(*args, **kwargs):
        print("wrap")
        x = f(*args, **kwargs)
        print(x)
        return x.upper()
    return wrap

@convert_upper
def my_name(name):
    print("my_name")
    return name


if __name__ == '__main__':
    print(my_name("joe"))
