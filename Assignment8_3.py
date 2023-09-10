
def Pattern(no):
    if no > 0:
        print((no), end = "    ")
        no -= 1
        Pattern(no)

def main():
    Num = int(input("Enter the number : "))

    Pattern(Num)

if __name__ == "__main__":
    main()