# https://github.com/carrocarros/lab11-CarolinaDagostin
# Carolina Dagostin
# No partner since there was an odd number in the class

import math
def square_root(a):
    if a < 0:
        raise ValueError("Can't take the square root of a negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    return math.log(a, b)

def exp(a, b):
    return a**b