# Non Encapsulated Banking System
class CustomerAccount:
    def __init__(self, customer_id: int, customer_name: str, account_balance: int):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.account_balance = account_balance
        self.transaction_log = TransactionLog()

    def deposit(self, amount: int):
        self.account_balance += amount
        self.transaction_log.log_transaction(f"Deposited {amount}")

    def withdraw(self, amount: int):
        self.account_balance -= amount
        self.transaction_log.log_transaction(f"Withdrew {amount}")


class TransactionLog:
    def log_transaction(self, transaction_details: str):
        self.transaction_details = transaction_details
        print(self.transaction_details)


customer = CustomerAccount(1, "Mia Miller", 50000)
customer.deposit(15000)
customer.withdraw(10000)
print(customer.account_balance)

# The system lets anyone directly change class properties, which can cause mistakes in how it works.
# Not controlling how data is changed can mess up account balances and make the banking system less reliable.
# Also, not checking if data is correct and showing transaction details openly can make the system less secure, risking financial errors and exposing private info.
