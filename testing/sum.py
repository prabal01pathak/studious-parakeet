#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sum of two numbers
author: prabal
'''
from .second import seconds

def sum(a, b):
    print("sum of two numbers")
    return a + b

def call_seconds():
    print("calling seconds")
    print(seconds())
