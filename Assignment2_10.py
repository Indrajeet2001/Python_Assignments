def Digit(No):
    iDigit = 0
    #iNum = 0
    iSum = 0
    while No != 0:
        iDigit = int(No % 10)
        iSum = iSum + iDigit
        No = No / 10
    return iSum

def main():
 
    print("Enter the number :")
    Num = int(input())

    Result = Digit(Num)

    print("Addition of all the digits is : ",Result)
    
        
if __name__ == "__main__":
    main()