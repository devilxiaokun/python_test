class BankAccount():

    def __init__(self, name, account, balance ):
        self.name    = name
        self.account = account
        self.balance = balance

    def withdraw(self, money):
        self.balance = self.balance - money

    def save(self, money):
        self.balance = self.balance + money

    def __str__(self):
        return '---BankInfo---\nname: %s\naccount: %s\nbalance: $%d\n--------------'%(self.name,self.account,self.balance)

