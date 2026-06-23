# Student Management System

import json

students = []
modified = False

def read_data():
    try:
        # Opening a file and reading it with JSON module
        with open("students.json", 'r') as file:
            text = json.load(file)
        return text

    except(FileNotFoundError, json.JSONDecodeError):
        # Creating a file and writing it with JSON module
        with open("students.json", 'w') as file:
            json.dump([], file)
        return []


def write_data(students):
    # Saving data to JSON file
    with open("students.json", "w") as file:
        json.dump(students, file)

    print("Saved to file successfully.")

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
        print("Name updated successfully", end="\n\n")
    else:
        print("No student found.")
        print()

def main(modified):
    print("==========================\nStudent Management System\n==========================")
    students = read_data()
    while True:

        choice = "1) View Students\n2) Add Student\n3) Delete Student\n4) Search Student\n5) Update Student\n6) Write to file\n0) Exit"
        print(choice)

        usr_inp = input("Enter your choice (0-6): ")
        print()

        try:
            usr_inp = int(usr_inp)

            if(usr_inp == 0):
                if(modified):
                    ans = input("Would you like to save before exiting? (y/n): ").strip().lower()

                    if(ans == "y"):
                        write_data(students)
                        break
                    elif(ans == "n"):
                        break
                    else:
                        print("Please enter yes or no.")
                else:
                    break

            
            match(usr_inp):
                case 1:
                    view_students(students)
                case 2:
                    modified = True
                    add_student(students)
                case 3:
                    modified = True
                    delete_student(students)
                case 4:
                    search_student(students)
                case 5:
                    modified = True
                    update_student(students)
                case 6:
                    write_data(students)
                    modified = False
                case _:
                    print("Invalid choice")

        except ValueError:
            print("Enter value from 0 to 6")

main(modified)
