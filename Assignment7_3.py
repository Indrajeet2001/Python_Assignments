import threading

def EvenList(Brr):
    print("Addition of all the even elements is : ")
    EvenAdd = 0
    for i in range(len(Brr)):
        if(Brr[i] % 2 == 0):
            EvenAdd = EvenAdd + Brr[i]
    print(EvenAdd)


def OddList(Brr):
    print("Addition of all the odd elements is : ")
    OddAdd = 0
    for i in range(len(Brr)):
        if(Brr[i] % 2 != 0):
            OddAdd = OddAdd + Brr[i]
    print(OddAdd)

def main():
    size = int(input("Enter the number of elements in the list : "))

    Arr = list()

    print("Enter the elements : ")
    for i in range(size):
        Value = int(input())
        Arr.append(Value)

    thread1 = threading.Thread(target = EvenList, args = (Arr,))

    thread2 = threading.Thread(target = OddList, args = (Arr,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()