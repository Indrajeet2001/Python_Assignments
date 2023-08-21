def Pattern(No):
    Sum = 0
    for i in range(No):
        for j in range(No):
            if(i + j < 5):
                print("*", end = "    ")
        print("")    

def main():
 
    print("Enter the number :")
    Num = int(input())

    Pattern(Num)
    
        
if __name__ == "__main__":
    main()