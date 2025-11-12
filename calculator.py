import math
def square_root(a):
    if a < 0:
        raise ValueError("Can't take the square root of a negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        print("Invalid input.")
        return None

def exp(a, b):
    return a**b