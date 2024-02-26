class ATM:
    def _init_(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"



atm = ATM(1000)
print(atm.check_balance())  
print(atm.deposit(500))  
print(atm.withdraw(200))  
print(atm.check_balance())  