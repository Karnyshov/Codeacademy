class BankAccount:
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "The bank account belongs to {0} and current balance is {1}".format(self.name, self.balance)

    def show_balance(self):
        print("The current balance is {}".format(self.balance))

    def deposit(self, amount):
        if amount <= 0:
            print("Amount of money is negative or 0!")
        else:
            print("Adding {} dollars to bank account...".format(amount))
            self.balance += amount
            print(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Cannot take more money than you have!")
            return
        else:
            print("Withdrawing {} dollars from bank account...".format(amount))
            self.balance -= amount
            print(self.balance)


my_account = BankAccount("Bob")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)
