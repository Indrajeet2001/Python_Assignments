def Prime(No):
    Sum = 0
    for i in range(2,No,1):
        if(No % i != 0):
            return True
        else:
            return False

def main():
 
    print("Enter the number :")
    Num = int(input())

    Result = Prime(Num)
    if(Result == True):
        print("It is Prime Number")
    else:
        print("It is not a Prime Number")
        
if __name__ == "__main__":
    main()