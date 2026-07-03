class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 5)
v2 = Vector(3, 7)

print(v1 + v2)

class ShoppingCart:
    def __init__(self, total):
        self.total = total

    def __add__(self, other):
        return ShoppingCart(self.total + other.total)

    def __str__(self):
        return f"Total: ₹{self.total}"

cart1 = ShoppingCart(230)
cart2 = ShoppingCart(270)

cart3 = cart1 + cart2

print(cart3)