# A calculator library

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if(n2 == 0):
        return "Cannot divide by zero."
    return n1 / n2

def modulus(n1, n2):
    if(n2 == 0):
        return "Cannot mod by zero."
    return n1 % n2