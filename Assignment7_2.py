import threading

def EvenFactor(No):
    print("Addition of all the even factors is : ")
    EvenAdd = 0
    for i in range(1,No,1):
        if(No % i == 0):
            if(i % 2 == 0):
                EvenAdd = EvenAdd + i
    print(EvenAdd)


def OddFactor(No):
    print("Addition of all the odd factors is : ")
    OddAdd = 0
    for i in range(1,No,1):
        if(No % i == 0):
            if(i % 2 != 0):
                OddAdd = OddAdd + i
    print(OddAdd)

def main():
    Num = int(input("Enter the number : "))

    thread1 = threading.Thread(target = EvenFactor, args = (Num,))

    thread2 = threading.Thread(target = OddFactor, args = (Num,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main thread")
if __name__ == "__main__":
    main()