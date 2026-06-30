class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if(isinstance(value, str) and value.strip()):
            self.__name = value
        else:
            print("Invalid name.")

student = Student("Gourav")

print(student.name)

student.name = "Sher"
print(student.name)

student.name = ""
student.name = 123
student.name = "   "

print(student.name)