class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Money added successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if(amount > 0):
            if(self.__balance >= amount):
                self.__balance -= amount
                print("Money deducted.")
            else:
                print("Not enough balance")
        else:
            print("Invalid withdrawal amount.")

    def show_balance(self):
        return self.__balance


account = BankAccount()
print(f"Balance: {account.show_balance()}")

account.deposit(500)
print(f"Balance: {account.show_balance()}")

account.withdraw(300)
print(f"Balance: {account.show_balance()}")

account.withdraw(1000)
account.deposit(-50)
account.withdraw(-20)

print(f"Final Balance: {account.show_balance()}")