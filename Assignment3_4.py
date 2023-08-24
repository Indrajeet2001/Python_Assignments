def Maximum(Arr, No):
    Cnt = 0
    for i in range(len(Arr)):
        if(Arr[i] == No):
            Cnt += 1
    return Cnt

def main():
    Size = int(input("Enter the size of the list : "))

    Arr = list()

    print("Enter the elements of the list : ")
    for i in range(Size):
        value = int(input())
        Arr.append(value)
    
    Num = int(input("Enter another number to check the frequency : "))

    result = Maximum(Arr, Num)
    print("Frequency of the number is : ",result)
        
if __name__ == "__main__":
    main()