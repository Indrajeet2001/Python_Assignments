i = 0

def Pattern(no):
    global i
    if i < no:
        print("*", end = "    ")
        i += 1
        Pattern(no)

def main():

    Num = int(input("Enter the number : "))

    Pattern(Num)

if __name__ == "__main__":
    main()