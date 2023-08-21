from Arithmetic import Add
from Arithmetic import Sub
from Arithmetic import Mult
from Arithmetic import Div

def main():

    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Result = Add(Value1, Value2)
    print("Addition is : ",Result)

    Result = Sub(Value1, Value2)
    print("Subtraction is : ",Result)

    Result = Mult(Value1, Value2)
    print("Multiplication is : ",Result)

    Result = Div(Value1, Value2)
    print("Division is : ",Result)

if __name__ == "__main__":
    main()