# ---------------------------------------------------------------------
# Unit Testing Your Code with the unittest Module
# https://www.youtube.com/watch?v=6tNS--WetLI
# ---------------------------------------------------------------------

# suppose we have following function
def add (x, y):
    return x + y

def subtract (x, y):
    return x - y;

def multiply (x, y):
    return x * y;

def divide (x, y):
    if y == 0:
        raise ValueError ('Can not divide by zero!')
    return x / y;

# you can use print statement to do your manual testing
# but it is not scalable
# e.g. print(subtract(10, 5))
# see test_calc.py