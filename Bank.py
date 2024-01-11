# Bank.py
from User import User
from Account import Account
from Transaction import Transaction

class Bank:
    def __init__(self):
        self.users = []
        self.accounts = []
        self.transactions = []

    def create_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_account(self, user, initial_balance=0):
        account = Account(user, initial_balance)
        self.accounts.append(account)
        return account

    def transfer(self, source_account, destination_account, amount):
        if source_account.withdraw(amount):
            destination_account.deposit(amount)
            transaction = Transaction(source_account, destination_account, amount)
            self.transactions.append(transaction)

    def display_users(self):
        print("Users:")
        for user in self.users:
            print(f"Username: {user.get_username()}, Email: {user.get_email()}")
        print()

    def display_accounts(self):
        print("Accounts:")
        for account in self.accounts:
            user = account.get_user()
            print(f"User: {user.get_username()}, Balance: ${account.get_balance():.2f}")
        print()

    def display_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            timestamp = transaction.get_timestamp()
            source_account = transaction.get_source_account()
            destination_account = transaction.get_destination_account()
            amount = transaction.get_amount()

            print(f"Timestamp: {timestamp}, Source Account: {source_account.get_user().get_username()}, "
                  f"Destination Account: {destination_account.get_user().get_username()}, Amount: ${amount:.2f}")
        print()

# Example usage
if __name__ == "__main__":
    bank = Bank()

    user1 = bank.create_user("john_doe", "john@example.com")
    user2 = bank.create_user("jane_doe", "jane@example.com")

    account1 = bank.create_account(user1, 1000.0)
    account2 = bank.create_account(user2, 500.0)

    bank.display_users()
    bank.display_accounts()

    bank.transfer(account1, account2, 200.0)

    bank.display_accounts()
    bank.display_transactions()
