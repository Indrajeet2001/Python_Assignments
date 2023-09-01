import threading

def Small(str):
    Cnt = 0
    for i in range(len(str)):
        if('a' <= str[i] <= 'z'):
            Cnt += 1
    print("The number of small alphabets are : ",Cnt)
    print("Thread ID of Small case thread is : ",threading.get_ident())
    print("The name of the thread is : ",threading.current_thread().name)

def Capital(str):
    Cnt = 0
    for i in range(len(str)):
        if('A' <= str[i] <= 'Z'):
            Cnt += 1
    print("The number of Capital alphabets are : ",Cnt)
    print("Thread ID of Capital thread is : ",threading.get_ident())
    print("The name of the thread is : ",threading.current_thread().name)

def Digits(str):
    Cnt = 0
    for i in range(len(str)):
        if('0' <= str[i] <= '9'):
            Cnt += 1
    print("The number of Digits are : ",Cnt)
    print("Thread ID of Digits thread is : ",threading.get_ident())
    print("The name of the thread is : ",threading.current_thread().name)


def main():
    Str = input("Enter the string : ")    

    thread1 = threading.Thread(target = Small, args = (Str,))

    thread2 = threading.Thread(target = Capital, args = (Str,))

    thread3 = threading.Thread(target = Digits, args = (Str,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()