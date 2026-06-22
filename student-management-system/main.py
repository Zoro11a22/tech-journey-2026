# Student Management System

students = []

def view_students(students):
    if not students:
        print("No students found.")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student}")
    print()

def add_student(students):
    stu_name = input("Enter student name: ")
    students.append(stu_name)
    print()

def delete_student(students):
    stu_name = input("Enter student name: ")
    if( stu_name in students ):
        students.remove(stu_name)
    print("Student deleted successfully.")
    print()

def search_student(students):
    stu_name = input("Enter student name: ")
    if( stu_name in students ):
        print(stu_name)
    else:
        print("Not in list.")
    print()

def update_student(students):
    stu_name = input("Enter student name: ")
    if( stu_name in students ):
        indx = students.index(stu_name)
        new_stu_name = input("Enter updated student name: ")
        students[indx] = new_stu_name
    else:
        print("Not in list.")
    print()

def main():
    while True:
        print("Welcome to Student Management System!")

        choice = """1) View Students
2) Add Student
3) Delete Student
4) Search Student
5) Update Student
0) Exit"""
        print(choice)

        user_inp = input("Enter your choice(01-05): ")
        print()

        try:
            user_inp = int(user_inp)
            if(user_inp == 0):
                break

            match(user_inp):
                case 1:
                    view_students(students)
                case 2:
                    add_student(students)
                case 3:
                    delete_student(students)
                case 4:
                    search_student(students)
                case 5:
                    update_student(students)
                case _:
                    print("Invalid choice")

        except ValueError:
            print("Enter value from 0 to 5")

main()