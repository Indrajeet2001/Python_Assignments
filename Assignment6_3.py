
class Numbers:

    def __init__(self,A):
        self.Value = A
    
    def ChkPrime(self):
        self.Cnt = 0
        for i in range(2,self.Value,1):
            if(self.Value % i == 0):
                self.Cnt += 1
        if(self.Cnt == 0):
            return True
        else:
            return False
    
    def ChkPerfect(self):
        self.Add = 0
        for i in range(1,self.Value,1):
            if(self.Value % i == 0):
                self.Add = self.Add + i
        if(self.Add == self.Value):
            return True
        else:
            return False
        
    def SumFactors(self):
        self.Add = 0
        for i in range(1,self.Value,1):
            if(self.Value % i == 0):
                self.Add = self.Add + i
        return self.Add
    
    def Factors(self):
        for i in range(1,self.Value,1):
            if(self.Value % i == 0):
                print("Factoes are : ",i)
    
def main():

    Num = int(input("Enter the number : "))
    
    obj1 = Numbers(Num)

    Ret = obj1.ChkPerfect()
    if(Ret == True):
        print("Number is Perfect Number")
    else:
        print("Number is not Perfect Number")    

    Ret = obj1.ChkPrime()
    if(Ret == True):
        print("Number is Prime Number")
    else:
        print("Number is not Prime Number")    

    Ret = obj1.SumFactors()
    print("Sum of all the factors is : ",Ret)

    obj1.Factors()

if __name__ == "__main__":
    main()