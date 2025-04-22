class InvalidAmount(Exception):
    def __init__(self, message='Invalid Amount!'):
        super().__init__(message)

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name        
        self.transactions = []

    def invalidAmount(self):
        raise InvalidAmount
    
    def showTransaction(self):
        print(f"Initial Balance: {self.balance - sum(self.transactions)}")
        for t in self.transactions:
            action = "deposited" if t>0 else "withdrawn"
            print(f"Amount {action}: {abs(t)}")
        print(f"Current Balance: {self.balance}")
        
        

class Customer(Bank):
    def __init__(self, bank_name: str, balance=0):
        super().__init__(bank_name)
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmount
        else:
            self.balance += amount
            self.transactions.append(amount)

    def withdraw(self, amount):
        if (amount <= 0 or amount > self.balance):
            raise InvalidAmount
        else:
            self.balance -= amount
            self.transactions.append(-1*amount)

hdfc = Bank("HDFC")
raj = Customer('HDFC', 100)
raj.deposit(5000)
raj.withdraw(3000)
print(raj.balance)
print(raj.showTransaction())
