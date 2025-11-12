import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("Invalid input.")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        print("Invalid input.")

def exp(a, b):
    return a**b