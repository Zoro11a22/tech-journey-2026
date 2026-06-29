class Student:
    school = "ABC College"

    def __init__(self, name):
        self.name = name


stu1 = Student("Sher")
stu2 = Student("Raj")

print(stu1.school)
print(stu2.school)

stu1.school = "XYZ School"

print(stu1.school)

Student.school = "XYZ University"

print(stu1.school)
print(stu2.school)