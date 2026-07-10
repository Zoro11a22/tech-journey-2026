class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")

        self._balance = amount

bank = BankAccount()
bank.balance = 100

print(bank.balance)

class MathUtils:

    @staticmethod
    def square(num):
        return num**2

    @staticmethod
    def cube(num):
        return num**3

print(MathUtils.square(5))
print(MathUtils.cube(3))

class Book:
    library = "Central Library"

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def change_library(cls, name):
        cls.library = name

    @classmethod
    def from_string(cls, data):
        title, author = data.split(",")
        return cls(title, author)

Book.change_library("National Library")
print(Book.library)

book1 = Book.from_string("The Great Book,Me")

print(book1.title)
print(book1.author)