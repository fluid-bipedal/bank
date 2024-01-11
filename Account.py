# Account.py
class Account:
    def __init__(self, user, balance=0):
        self.user = user
        self.balance = balance

    def get_user(self):
        return self.user

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False
