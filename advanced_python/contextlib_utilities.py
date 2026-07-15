from contextlib import closing, suppress, redirect_stdout
import os
from io import StringIO

class FakeConnection:
    def __init__(self):
        print("Connecting...")

    def execute(self, query):
        print(f"Executing: {query}")

    def close(self):
        print("Connection closed.")

with closing(FakeConnection()) as conn:
    conn.execute("SELECT * FROM users")

with suppress(FileNotFoundError):
    os.remove("temporary_file.txt")

print("Cleanup finished.")

def display_menu():
    print("==== MENU ====\n1. Start\n2. Settings\n3. Exit")

buffer = StringIO()

with redirect_stdout(buffer):
    display_menu()

captured = buffer.getvalue()

print(f"Captured Output:\n{captured}")

with open("menu.txt", "w") as file, redirect_stdout(file):
    display_menu()

print("Menu saved successfully.")