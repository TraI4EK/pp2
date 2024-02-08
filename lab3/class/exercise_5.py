class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount_of_deposit = float(input("Enter the amout you would deposit: "))
        if amount_of_deposit <= 0:
            print("Invalid input, please try again.")
            return self.deposit()
        self.balance += amount_of_deposit
        print(f"Balance has been updated. Your balance = {self.balance}")

    def withdraw(self):
        amount_of_withdraw = float(input("Enter the amout you would withdraw: "))
        if amount_of_withdraw <= 0:
            print("Invalid input, please try again.")
            return self.withdraw()
        if amount_of_withdraw > self.balance:
            print("Insufficient funds. Operation is not available.")
            return self.withdraw()
        self.balance -= amount_of_withdraw
        print(f"Withdraw operation was successful. Your balance = {self.balance}")

account_use = Account("Vladlen", 124)
account_use.deposit()
account_use.withdraw()