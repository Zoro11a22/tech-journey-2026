from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()

    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"Elapsed: {end-start:.5f} seconds.")

with timer():
    total = sum(range(10_000_000))

@contextmanager
def managed_file(filename, mode):
    print("Opening file...")

    file = open(filename, mode)

    try:
        yield file
    finally:
        file.close()
        print("Closing file...")

with managed_file("notes.txt", "w") as f:
    f.write("Hello Contextlib!")

with managed_file("notes.txt", "r") as f:
    print(f.read())

with managed_file("notes.txt", "w") as f:
    f.write("Testing")
    raise RuntimeError("Boom!")