class account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep):
        self.balance += dep
        return "accepted"
    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print("request exceeds the current balance")
        else:
            self.balance -= withdraw
        return self.balance
bank=account("zhandar",20000)
print(bank.deposit(10000))
print(bank.withdraw(10000))