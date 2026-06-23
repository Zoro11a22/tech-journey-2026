# Student Management System

students = []

def find_student(students): 
    usr_inp = input("Enter student name: ").strip()

    # Get dictionary within list with index
    for index, values in enumerate(students):

        # Map all names to "value" one by one for comparison
        value = values["name"]

        # Check if name provided by user is within the list and return the values if true
        if(usr_inp.lower() == value.lower()):
            return index, value, True
    # Return none for placeholders and false for terminating calls
    if(not stu_found):
        return None, None, False

def view_students(students):

    # Return "No students found" if list is empty and end the function
    if not students:
        print("No students found.", end="\n\n")
        return None
    
    # Heading
    print("   Name    Age    RollNo")

    for index, value in enumerate(students):
        # Print serial number
        print(f"{index+1}. ", end='')
        # Get all keys of iterating dictionary 
        for key in value.keys():
            # Print the values of iterating dictionary using its keys
            print(f"{value[key]}", end="    ")

        print(end="\n\n")

def add_student(students):
    try:
        stu_name = input("Enter student name: ").strip()
        stu_age = int(input("Enter student age: "))
        stu_roll = int(input("Enter student roll number: "))

        # Running check to stop duplicate roll numbers
        while True:
            new_roll = True
            for values in students:
                # Mapping roll numbers to "value"
                value = values["roll"]
                # Confirming if roll number already exists
                if(stu_roll == value):
                    new_roll = False
                    # Asking for new roll number
                    print("Roll number not available. Please chose different one!")
                    stu_roll = int(input("Enter new roll number: "))
            # Breaking the while loop if roll number doesn't exist
            if(new_roll):
                break
            
        data = {}
        data["name"] = stu_name
        data["age"] = stu_age
        data["roll"] = stu_roll

        students.append(data)
        print()

    except ValueError:
        print("Please enter integers only for age and roll number.")

def delete_student(students):
    # Calling find function to fetch student details
    index, value, stu_found = find_student(students)
    if(stu_found):
        # Deleting the student's data if exists
        students.pop(index)
        print("Student deleted successfully.", end="\n\n")
    else:
        print("No students found.", end="\n\n")

def search_student(students):
    # Calling find function to fetch student details
    index, value, stu_found = find_student(students)
    if(stu_found):
        # Printing the student's data if exists
        print("Name    Age    RollNo")
        for key in students[index].keys():
            print(f"{students[index][key]}", end="    ")
        print(end="\n\n")
    else:
        print("No student found.")
        print()

def update_student(students):
    # Calling find function to fetch student details
    index, value, stu_found = find_student(students)
    if(stu_found):
        usr_inp = input("Enter new name: ").strip()
        # Updating student name
        students[index]["name"] = usr_inp
        print("Name updated successfilly", end="\n\n")
    else:
        print("No student found.")
        print()

def main():
    while True:
        print("Welcome to Student Management System!")

        choice = "1) View Students\n2) Add Student\n3) Delete Student\n4) Search Student\n5) Update Student\n0) Exit"
        print(choice)

        usr_inp = input("Enter your choice(01-05): ")
        print()

        try:
            usr_inp = int(usr_inp)

            if(usr_inp == 0):
                break
            
            match(usr_inp):
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