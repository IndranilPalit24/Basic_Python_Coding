class Bank:

    #this is a constructor
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    #to add deposit in the bank account
    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        if(amount>self.balance):
            print("Balance amount is less so you cannot withdraw the amount")
        else:
            self.balance-=amount
        return self.balance

#create an account in bank class
name = input("Enter your name: ")
b=Bank(name)

print(f"Hi {name} please Enter the details")

while(True):
    print('D - For Deposit\nW - WithDraw\nE - Exit')
    choice = input("Input your choice: ")

    if choice == 'e' or 'E':
        print("You have exited the system")
    
    amt = float(input("Enter the amount: "))

    if choice == 'd' or 'D':
        print("Balance after Deposit: ",b.deposit(amt))
    elif choice == 'W' or 'w':
        print("Balance after withdraw: ",b.withdraw(amt))



