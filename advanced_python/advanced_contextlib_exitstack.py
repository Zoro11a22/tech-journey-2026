from contextlib import ExitStack

class Worker():
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Starting: {self.name}")
        return self

    def work(self):
        print(f"{self.name} is working")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Stopping {self.name}")

try:
    with ExitStack() as stack:
        stack.callback(lambda: print("Final cleanup complete."))
        
        w1 = stack.enter_context(Worker("Database"))
        w2 = stack.enter_context(Worker("Network"))
        w3 = stack.enter_context(Worker("Logger"))

        w1.work()
        w2.work()
        w3.work()

        raise RuntimeError("Unexpected error")

except RuntimeError as err:
    print(f"Caught: {err}")