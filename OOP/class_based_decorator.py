from functools import update_wrapper

class Uppercase:
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result

@Uppercase
def greet(name):
    return f"Hello {name}"

print(greet("Zoro"))