def Add(Arr):
    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    return Sum

def main():
    Size = int(input("Enter the size of the list : "))

    Arr = list()

    print("Enter the elements of the list : ")
    for i in range(Size):
        value = int(input())
        Arr.append(value)
    
    result = Add(Arr)
    print("Addition of all the elements is  : ",result)
        
if __name__ == "__main__":
    main()