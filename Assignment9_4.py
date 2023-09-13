import os.path
import shutil

def main():
    print("Enter the names of the files that you want to compare : ")
    File1_name,File2_name = input(),input()

    if(os.path.exists(File1_name) & os.path.exists(File2_name)):
        fobj1 = open(File1_name, "r")
        fobj2 = open(File2_name, "r")

        Cnt = 0
        for L1 in fobj1:
            for L2 in fobj2:
                if(L1 != L2):
                    Cnt += 1
        if(Cnt == 0):
            print("Success")
        else:
            print("Failure")
    else:
        print("Invalid File name")
        
if __name__ == "__main__":
    main()