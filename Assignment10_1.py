from sys import *
import os

def DirectoryFileSearch(DirName, file_extension):
    print("We are going to Scan the directory : ",DirName)

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if (exist == True):
        for foldername,subfoldername,filename in os.walk(DirName):
            print("Current Directory name : ",foldername)

            print("Name of the files that matches the given extension is : ")

            for fname in filename:
                name,ext = os.path.splitext(fname)
                if(ext == file_extension):
                    print(fname)

def main():
    print("--------------Automation Script--------------")

    print("Automation Script name : ",argv[0])

    if(len(argv) != 3):
        print("invalid no of arguments")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):     # Flag for displaying help
        print("This automation script is used to display all the files of a given extension present inside a given directory")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):     # Flag for displaying usage of script
        print("Usage : Name_of_the_Script Frist_argument Second_argument")
        exit()
    try:
        DirectoryFileSearch(argv[1], argv[2])
    
    except ValueError : 
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)
    
if __name__ == "__main__":
    main()