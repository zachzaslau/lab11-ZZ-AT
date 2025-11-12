# https://github.com/zachzaslau/lab11-ZZ-AT/tree/main
# Partner 1: Zach Zaslau
# Partner 2: Anthony Toscano

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        return False

def hypotenuse(a, b): return math.hypot(a, b)

def add(a, b): return a + b
def subtract(a, b): return a - b
def mul(a, b): return a * b
def exp(a, b): return a ** b
def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
<<<<<<< HEAD
    except ZeroDivisionError:
        return False

def log(a, b):
    try:
        if b <= 0 or a <= 0:
            raise ValueError
=======
def logarithm(a, b):
    if b <= 0 or a <= 0:
        raise ValueError
    else:
>>>>>>> 822868cb8522e16cacb8b62e28199399b85eff49
        return math.log(b, a)
    except ValueError:
        return False




