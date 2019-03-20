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

class CheckingAccount(Account):

    def __init__(self, filepath, fee):     # self passed even if sub-class
        Account.__init__(self, filepath)  # invoking base account
        self.fee = fee                  # NB instance variable from constructor into sub-class

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

account = Account('balance.txt')         # instantiate
print(account)  # diagnostic
print(account.balance)
account.withdraw(100)
print(account.balance)
account.commit()

checking = CheckingAccount('balance.txt', 50)
print(checking.balance)
checking.deposit(100)
checking.commit()
print(checking.balance)
checking.transfer(300)
checking.commit()
print(checking.balance)
