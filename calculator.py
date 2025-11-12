import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError
    else:
        return a/b

def log(a,b):
    if b<=0 or a<=0:
        raise ValueError
    else:
        return math.log(b,a)

