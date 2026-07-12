import time

class Logger:
    def __enter__(self):
        print("Starting...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Finished...")

with Logger():
    print("Doing work...")

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()
        print(f"Elapsed: {self.end - self.start:.5f} seconds")

with Timer():
    print("Yo")

class Database:
    def __enter__(self):
        print("Connecting...")
        return self

    def query(self, command):
        print(f"Executing: {command}")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnecting...")

with Database() as db:
    db.query("SELECT * FROM users")