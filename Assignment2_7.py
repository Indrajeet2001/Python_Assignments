def Pattern(No):
    Sum = 0
    for i in range(No):
        for j in range(1,No+1,1):
            print(j, end = "    ")
        print("")    

def main():
 
    print("Enter the number :")
    Num = int(input())

    Pattern(Num)
    
        
if __name__ == "__main__":
    main()