class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print("Woof!")

dog = Dog("Buddy", "Golden Retriever")

print(dog.name)
print(dog.breed)

dog.eat()
dog.sleep()
dog.bark()