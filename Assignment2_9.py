def Digit(No):
    iCnt = 0
    while No != 0:
        iCnt += 1
        No = int(No / 10)
    return iCnt

def main():
 
    print("Enter the number :")
    Num = int(input())

    Result = Digit(Num)

    print("number of digits in the number are : ",Result)
        
if __name__ == "__main__":
    main()