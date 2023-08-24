from MarvellousNum import ChkPrime

def ListPrime(Arr):
    Sum = 0
    for i in range(len(Arr)):
        Ret = ChkPrime(Arr[i])
        if(Ret == True):
            Sum = Sum + Arr[i]            
    return Sum

def main():
    Size = int(input("Enter the size of the list : "))

    Arr = list()

    print("Enter the elements of the list : ")
    for i in range(Size):
        value = int(input())
        Arr.append(value)
    
    result = ListPrime(Arr)
    print("Summation of all the prime numbers is : ",result)
        
if __name__ == "__main__":
    main()