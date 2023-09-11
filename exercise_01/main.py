import BankAccount

account = BankAccount.BankAccount('William', 425.97)
account.deposit(125.03)
account.withdraw(331.75)
print(account.get_balance())