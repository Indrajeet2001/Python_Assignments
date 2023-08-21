def Fact(No):
    Mult = 1
    for i in range(No,0,-1):
        Mult = Mult * i
    return Mult

def main():

    print("Enter the number :")
    Num = int(input())

    Result = Fact(Num)
    print("Factorial is : ",Result)

if __name__ == "__main__":
    main()