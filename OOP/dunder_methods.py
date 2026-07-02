class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"Movie: {self.title} ({self.year})"

movie = Movie("Interstellar", 2014)

print(movie)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} earns ₹{self.salary}"
        
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"

emp = Employee("Alice", 50000)
emp2 = Employee("Zoro", 999999)

print(emp)

employees = [emp, emp2]

print(employees)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

print(len(cart))