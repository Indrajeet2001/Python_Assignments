
class BankAccount:
    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A
        self.Amount = B

    def Deposit(self,Value):
        self.Amount = self.Amount + Value

    def Withdraw(self,Value):
        if(Value > self.Amount):
            print("Insufficient Balance")
        else:
            self.Amount = self.Amount - Value

    def Display(self):
        print("Name of the Account Holder is : ",self.Name)
        print("Balance in the account is : ",self.Amount)

    def CalculateInterest(self):
        self.Interest = self.Amount * BankAccount.ROI
        self.Interest = self.Interest / 100
        return self.Interest

def main():
    obj1 = BankAccount("Sagar", 5000)
    obj1.Display()

    print("After Depositng 2000 into the Account")
    obj1.Deposit(2000)
    obj1.Display()

    print("After Withdrwaing 3000 from the Account")
    obj1.Withdraw(3000)
    obj1.Display()

    Ret = obj1.CalculateInterest()
    print("You will recieve interest of : ",Ret)

    obj2 = BankAccount("Amit", 7000)
    obj2.Display

    print("After Depositing 4000 into the Account")
    obj2.Deposit(4000)
    obj2.Display()

    print("After Withdrawing 2000 from the Account")
    obj2.Withdraw(2000)
    obj2.Display()

    Ret = obj2.CalculateInterest()
    print("You will recieve interest of : ",Ret)

if __name__ == "__main__":
    main()