# A basic calculator

def addition(n1, n2):
    return n1+n2

def subtraction(n1, n2):
    return n1-n2

def multiplication(n1, n2):
    return n1*n2

def division(n1, n2):
    return n1/n2


def main():

    print("======================\nWelcome to Calculator!\n======================")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print()
        print("1) Add (+)\n2) Subtract (-)\n3) Multiply (*)\n4) Divide (/)")
        opr = int(input("Enter operation ( 1-4 ): "))
        print()

    except ValueError:
        print("Enter integers only.")

    else:
        match opr:
            case 1:
                result = addition(num1, num2)
            case 2:
                result = subtraction(num1, num2)
            case 3:
                result = multiplication(num1, num2)
            case 4:
                try:
                    result = division(num1, num2)
                except ZeroDivisionError:
                    print("Cannot divide by 0.", end="\n\n")
                    
            case _:
                print("Enter value from 1 to 4")
                return

        print(f"The result is: {result}", end="\n\n")

    finally:
        print("================================\nThanks for using the Calculator.\n================================")

main()