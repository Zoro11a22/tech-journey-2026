class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.__available = True

    def borrow(self):
        if self.__available:
            self.__available = False
            print("Item borrowed.")
        else:
            print("Item is already borrowed.")

    def return_item(self):
        if not self.__available:
            self.__available = True
            print("Item returned.")
        else:
            print("Item was not borrowed.")          

    def is_available(self):
        return self.__available

    def __str__(self):
        return f"{self.title} ({self.year}) by {self.author}"

class Book(LibraryItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def __str__(self):
        status = "Available" if self.is_available() else "Borrowed"
        return f"Book: {super().__str__()} - {self.pages} pages [{status}]"

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def __str__(self):
        status = "Available" if self.is_available() else "Borrowed"
        return f"Magazine: {super().__str__()} - Issue #{self.issue_number} [{status}]"

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        if not self.items:
            print("Library is empty.")
            return
        for item in self.items:
            print(item)

    def borrow_item(self, title):
        title = title.strip().lower()
        for item in self.items:
            if item.title.lower() == title:
                item.borrow()
                return
        print("No such item found.")

    def return_item(self, title):
        title = title.strip().lower()
        for item in self.items:
            if item.title.lower() == title:
                item.return_item()
                return
        print("No such item found.")

library = Library()

book1 = Book("Atomic Habits", "James Clear", 2018, 320)

library.add_item(book1)

library.show_items()

library.borrow_item("Atomic Habits")

library.return_item("Atomic Habits")