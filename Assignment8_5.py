Fact = 1
i = 1

def Factorial(no):
    if(no == 0):
        return 0
    global Fact
    global i
    if no >= i:
        Fact = Fact * i
        i += 1
        Factorial(no)
    return Fact

def main():
    Num = int(input("Enter the number : "))

    Ret = Factorial(Num)

    print("Factorial of the number is : ",Ret)

if __name__ == "__main__":
    main()