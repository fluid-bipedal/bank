# Transaction.py
from datetime import datetime

class Transaction:
    def __init__(self, source_account, destination_account, amount):
        self.timestamp = datetime.now()
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount

    def get_timestamp(self):
        return self.timestamp

    def get_source_account(self):
        return self.source_account

    def get_destination_account(self):
        return self.destination_account

    def get_amount(self):
        return self.amount
