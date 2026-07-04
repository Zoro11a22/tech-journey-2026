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