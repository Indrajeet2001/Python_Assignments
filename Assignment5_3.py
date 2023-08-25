
class Arithmetic:
    def __init__(self):
        self.Value1 = 0.0
        self.Value2 = 0.0
    
    def Accept(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Division(self):
        return self.Value1 / self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
def main():

    Num1 = int(input("Enter the first value of : "))
    Num2 = int(input("Enter the second value of : "))

    obj1 = Arithmetic()

    obj1.Accept(Num1,Num2)

    ret = obj1.Addition()
    print("Addition is : ",ret)

    ret = obj1.Subtraction()
    print("Subtractio is : ",ret)

    ret = obj1.Division()
    print("Division is : ",ret)

    ret = obj1.Multiplication()
    print("Multiplicaion is : ",ret)

if __name__ == "__main__":
    main()