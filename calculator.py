import math
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
        print(f"Invalid input.")

def exp(a, b):
    return a**b
#meow