class Vehicle:
    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine started.")

car = Car()

car.start()

class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

circle = Circle()
rectangle = Rectangle()

shapes = [circle, rectangle]

for shape in shapes:
    shape.draw()