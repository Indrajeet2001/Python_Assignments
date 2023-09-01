import threading

def Thread1(No):
    for i in range(No+1):
        print("",i)

def Thread2(No):
    for i in range(No,0,-1):
        print("",i)

def main():
    Num = int(input("Enter the number : "))

    thread1 = threading.Thread(target = Thread1, args = (Num,))

    thread2 = threading.Thread(target = Thread2, args = (Num,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()