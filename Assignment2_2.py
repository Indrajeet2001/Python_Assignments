def Pattern(No):
    for i in range(No):
        print("*    *    *    *    *")

def main():
    Value = int(input("Enter the number of iterations : "))

    Pattern(Value)
    
if __name__ == "__main__":
    main()