#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A generator is a special type of function which does not return a single value, 
instead, it returns an iterator object with a sequence of values.
'''

def generator_f(x):
    while True:
        yield x
        x += 1
        yield x


iterable = generator_f(10)

for i in iterable:
    print(i)
