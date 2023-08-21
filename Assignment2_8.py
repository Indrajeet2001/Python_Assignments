def Pattern(No):
    k = 0
    for i in range(No):
        k = 1
        for j in range(No):
            if(i >= j):
                print(k, end = "    ")
                k += 1
        print("")    

def main():
 
    print("Enter the number :")
    Num = int(input())

    Pattern(Num)
    
        
if __name__ == "__main__":
    main()