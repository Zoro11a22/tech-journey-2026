from functools import wraps

def retry(times):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Attempt {i+1}")
                result = func(*args, **kwargs)
            return result
        return wrapper

    return decorator

@retry(3)
def connect():
    print("Connecting...")

connect()