
class Demo:
    Value = 0
    def __init__(self,A,B):
        print("Inside Contructor")
        self.No1 = A
        self.No2 = B
    
    def Fun(self):
        print(self.No1)
        print(self.No2)

    def Gun(self):
        print(self.No1)
        print(self.No2)

def main():

    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    obj1  = Demo(Value1,Value2)

    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    obj2 = Demo(Value1,Value2)

    obj1.Fun()
    obj1.Gun()

    obj2.Fun()
    obj2.Gun()

if __name__ == "__main__":
    main()