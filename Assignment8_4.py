Add = 0

def AddDigit(no):
    Digit = 0
    global Add
    if no != 0:
        Digit = int(no % 10)
        Add = Digit + Add
        no = int(no / 10)
        AddDigit(no)
    return Add

def main():
    Num = int(input("Enter the number : "))

    Ret = AddDigit(Num)

    print("Addition of all the digits is : ",Ret)

if __name__ == "__main__":
    main()