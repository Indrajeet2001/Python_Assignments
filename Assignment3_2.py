def Maximum(Arr):
    Max = Arr[0]
    for i in range(len(Arr)):
        if(Max < Arr[i]):
            Max = Arr[i]
    return Max

def main():
    Size = int(input("Enter the size of the list : "))

    Arr = list()

    print("Enter the elements of the list : ")
    for i in range(Size):
        value = int(input())
        Arr.append(value)
    
    result = Maximum(Arr)
    print("Largest element is  : ",result)
        
if __name__ == "__main__":
    main()