def Minimum(Arr):
    Min = Arr[0]
    for i in range(len(Arr)):
        if(Min > Arr[i]):
            Min = Arr[i]
    return Min

def main():
    Size = int(input("Enter the size of the list : "))

    Arr = list()

    print("Enter the elements of the list : ")
    for i in range(Size):
        value = int(input())
        Arr.append(value)
    
    result = Minimum(Arr)
    print("Smallest element is  : ",result)
        
if __name__ == "__main__":
    main()