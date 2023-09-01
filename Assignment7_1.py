import threading

def even(No):
    Cnt = 0
    for i in range(0,(No * 2),1):
        if(i % 2 == 0):
            print(" ",i)
            Cnt += 1


def odd(No):
    Cnt = 0
    for i in range(0,(No * 2),1):
        if(i % 2 != 0):
            print(" ",i)
            Cnt += 1

def main():
    Num = int(input("Enter the number : "))

    thread1 = threading.Thread(target = even, args = (Num,))

    thread2 = threading.Thread(target = odd, args = (Num,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()