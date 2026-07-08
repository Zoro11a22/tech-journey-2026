import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Runtime: {end - start:.5f} seconds")
        return result
    return wrapper

def print_status(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Finished...")

        return result

    return wrapper

@timer
@print_status
def hello():
    print("Hello World")

@timer
@print_status
def welcome(name):
    print(f"Welcome {name}")

hello()
welcome("Zoro")