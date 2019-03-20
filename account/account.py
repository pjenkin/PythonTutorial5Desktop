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
    ''' This class d'generate checking account objects '''
    # the above is a docstring
    type = 'checking-account'           # a class (not instance) variable
    
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

jack_checking = CheckingAccount('jack.txt', 50)
print(jack_checking.balance)
jack_checking.deposit(200)
jack_checking.commit()
print(jack_checking.balance)
jack_checking.transfer(300)
jack_checking.commit()
print(jack_checking.balance)
print(jack_checking.type)           # check class variable

john_checking = CheckingAccount('john.txt', 20)
print(john_checking.balance)
john_checking.deposit(100)
john_checking.commit()
print(john_checking.balance)
john_checking.transfer(200)
john_checking.commit()
print(john_checking.balance)
print(john_checking.type)
print(john_checking.__doc__)
