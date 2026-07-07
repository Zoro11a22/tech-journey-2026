class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.__available = True

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_item(self):
        if not self.__available:
            self.__available = True
            return True
        return False        

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
                if item.borrow():
                    print("Item borrowed.")
                else:
                    print("Item is already borrowed.")
                return
        print("No such item found.")

    def return_item(self, title):
        title = title.strip().lower()
        for item in self.items:
            if item.title.lower() == title:
                if item.return_item():
                    print("Item returned.")
                else:
                    print("Item is not borrowed.")
                return
        print("No such item found.")

    def __len__(self):
        return len(self.items)

    def search_item(self, title):
        title = title.strip().lower()
        found = False  
        for item in self.items:
            item_title = item.title.lower()
            if title in item_title:
                print(item)
                found = True
        if not found:
            print("No such item found.")

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        return f"Library with {len(self)} items"
            

library = Library()

library.add_item(Book("Dune", "Frank Herbert", 1965, 789))

print(library)

library.show_items()