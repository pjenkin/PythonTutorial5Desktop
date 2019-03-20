class Account:

    # whole currency units only

    # need to read & store balance value
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.balance = int(file.read())      # instance variable / property
        self.filepath = filepath

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))



account = Account('balance.txt')         # instantiate
print(account)  # diagnostic
print(account.balance)
account.withdraw(100)
print(account.balance)
account.commit()

