# Utility Toolkit

import operations
import converter
import greetings
import password_generator

def calculator_menu():
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        usr_inp = int(input("Choose an option (1-5): "))
        n1 = int(input("First Number: "))
        n2 = int(input("Second Number: "))

    except ValueError:
        print("Please enter integers only.")
        return

    match usr_inp:
            case 1:
                print(f"Result: {operations.add(n1, n2)}")
            case 2:
                print(f"Result: {operations.subtract(n1, n2)}")
            case 3:
                print(f"Result: {operations.multiply(n1, n2)}")
            case 4:
                print(f"Result: {operations.divide(n1, n2)}")
            case 5:
                print("Goodbye!")
            case _:
                print("Chose from 1 to 5 only.")



def converter_menu():
    print("\n===== Unit converter =====")
    print("1. Km to Miles")
    print("2. Miles to Km")
    print("3. °C to °F")
    print("4. °F to °C")
    print("5. Exit")

    try:
        usr_inp = int(input("Choose an option (1-5): "))
        n1 = int(input("Enter Value: "))

    except ValueError:
        print("Please enter integers only.")
        return

    match usr_inp:
            case 1:
                print(f"Result: {converter.kilometers_to_miles(n1)}")
            case 2:
                print(f"Result: {converter.miles_to_kilometers(n1)}")
            case 3:
                print(f"Result: {converter.celsius_to_fahrenheit(n1)}")
            case 4:
                print(f"Result: {converter.fahrenheit_to_celsius(n1)}")
            case 5:
                print("Goodbye!")
            case _:
                print("Chose from 1 to 5 only.")

def greeter_menu():
    print("\n===== Greeter =====")
    print(f"Hello there, {greetings.greeter()}")

def pass_gen_menu():
    print("\n===== Password Generator =====")

    try:
        length = int(input("Enter password length: "))
        if(length < 8):
            print("Length must be more than 7.")
            return
    except ValueError:
        print("Enter integers only.")
        return

    upper = input("Include uppercase letters (y/n): ").strip().lower()
    lower = input("Include lowercase letters (y/n): ").strip().lower()
    num = input("Include numbers (y/n): ").strip().lower()
    symbol = input("Include special characters (y/n): ").strip().lower()

    if(upper == "y" or lower == "y" or num == "y" or symbol == "y"):
        if(upper == "y"):
            upper = True
        if(lower == "y"):
            lower = True
        if(num == "y"):
            num = True
        if(symbol == "y"):
            symbol = True
        
    elif(upper == "n" and lower == "n" and num == "n" and symbol == "n"):
        print("At least one character type must be selected.")
    else:
        print("Please enter valid input.")

    print(f"Your password is: {password_generator.pass_gen(length, upper, lower, num, symbol)}")

def menu():
    print("\n===== Utility Toolkit =====")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Greeting Generator")
    print("4. Password Generator")
    print("5. Exit")

def main():
    while True:

        menu()

        try:
            choice = int(input("Choose an option (1-5): "))
        except ValueError:
            print("Please enter integers only.")

        match choice:

            case 1:
                calculator_menu()
            case 2:
                converter_menu()
            case 3:
                greeter_menu()
            case 4:
                pass_gen_menu()
            case 5:
                print("Goodbye!")
                break

            case _:
                print("Chose from 1 to 5 only.")

main()