import os.path
import shutil

def main():
    print("Enter the name of the file that you want to read : ")
    File1_name = input()

    print("Enter the string that you want to check : ")
    Str = input()

    if(os.path.exists(File1_name)):
        fobj = open(File1_name, "r")

        Cnt = 0
        for line in fobj:
            for word in line.split():
                if(word == Str):
                    Cnt += 1
        print("Frequency of the string in the file is : ",Cnt)
    else:
        print("File does not exist")
        
if __name__ == "__main__":
    main()