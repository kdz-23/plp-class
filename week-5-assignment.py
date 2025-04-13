
""" Week 5 OOP concepts in python"""

# Base class (BankAccount class)

class BankAccount:
    def __init__(self, customer_name, account_number, balance=0):
        self.customer_name = customer_name
        self.account_number = account_number
        self._balance = balance
    
    # Class methods:

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ksh{amount}, New balance is: ksh{self._balance}")
        else:
            print("Deposit Failed!, Invalid amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Successfuly withdraw ksh{amount}. New balance is: ksh{self._balance}")
        else:
            print("Withdraw Failed!, Insuficient or invalid amount")
    
    def check_balance(self):
        print(f"Dear {self.customer_name}, your account balance is: {self._balance}")
        return self._balance
    
    # Inheritance (Saving Account)
class SavingAccount(BankAccount):
    def __init__(self, customer_name, account_number, balance=0, intrest_rate=0.05):
        super().__init__(customer_name, account_number, balance)
        self.intrest_rate = intrest_rate
        print(f"Dear {self.customer_name}, You have successfully created a saving account.")
    
    def apply_intrest(self):
        intrest = self._balance * self.intrest_rate
        self._balance += intrest
        print(f"Saving account balance: ksh{self._balance}")


# Usage 
if __name__ == '__main__':
    customer = input("Customer Name: ")
    account = int(input("Account Number: "))
    
    my_account = BankAccount(customer, account)
    saving_account = SavingAccount(customer, account)

    my_account.deposit(4300)
    my_account.check_balance()







