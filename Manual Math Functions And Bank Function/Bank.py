class BankAccount:
    def __init__(self):
        self.balance = 0
        self.interest1=0
    def deposit(self):
        inputAmount = int(input("Please enter the amount of money you want to deposit : "))
        self.balance+=inputAmount
        print("Your balance is {}".format(self.balance))
    def withdraw(self):

        inputAmount = int(input("Please enter the amount of money you want to withdraw : "))

        if self.balance>=inputAmount:
            self.balance-=inputAmount
            print("Your remaining balance is {}".format(self.balance))
            return self.balance

        else:
            print("Your balance is lower than withdraw amount!!")
    def interest(self):
        self.interest1=(self.balance/1000)*3
        print("Your interest is {}".format(self.interest1))
    def display(self):
        interest=self.interest1
        self.balance+=interest
        print("Your current balance is : {}".format(self.balance))
