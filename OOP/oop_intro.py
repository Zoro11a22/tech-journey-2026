class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

dog1 = Dog("Rocky", "Labrador")
# dog2 = Dog()

# print(dog1)
# print(dog2)

# print(dog1 == dog2)
# print(dog1 is dog2)

dog1.bark()

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name}.\nI am {self.age} years old.")

stu1 = Student("Sher", 20)
stu2 = Student("Raj", 18)

# print(stu1.name)
# print(stu1.age)
# print(stu2.name)


stu1.introduce()
stu2.introduce()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect1 = Rectangle(7, 5)
rect2 = Rectangle(12, 8)

# print(rect1.length)
# print(rect1.width)
# print(rect2.length)
# print(rect2.width)

print(f"Area of rectangle: {rect1.area()}")
print(f"Area of rectangle: {rect2.area()}")