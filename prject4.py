# Bank account management system
"""
1. Bank Account Simulator
Concepts: Classes, methods, instance variables

What to build:

BankAccount class with methods: deposit(), withdraw(), check_balance()

Track account holder's name and balance

Bonus: Add overdraft protection or transaction history

"""
class BankAccount:
    def __init__(self,owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            print("The amount of the deposit must be positive.")
        else:
            self.balance  = self.balance + amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        return self.balance
    
    def withdow(self, amount):
        if amount < 0:
            print("The amount of the withdrawal must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        return self.balance
    
    def get_balance(self):
        return self.balance
    

initial_balance = input("Enter the initial balance for the account: ")
account = BankAccount("John Doe", float(initial_balance))

while True:
    print("\nBank Account Management")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        account.withdow(amount)
    elif choice == '3':
        print(f"Current balance: {account.get_balance()}")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid option, please try again.")
