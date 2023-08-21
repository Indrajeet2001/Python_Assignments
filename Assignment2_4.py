def Fact(No):
    Sum = 0
    for i in range(1,No,1):
        if(No % i == 0):
            Sum = Sum + i
    return Sum

def main():

    print("Enter the number :")
    Num = int(input())

    Result = Fact(Num)
    print("Addition of Factors is : ",Result)

if __name__ == "__main__":
    main()