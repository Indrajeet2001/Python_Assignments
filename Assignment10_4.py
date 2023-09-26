from sys import *
import os
import shutil

def DirectoryCopy(DirName, DirName_new, extension):
    print("We are going to Scan the directory : ",DirName)

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if (exist == True):
        print("Current Directory name : ",DirName)

        flag = os.path.isabs(DirName_new)

        if flag == False:
            DirName_new = os.path.abspath(DirName_new)

        #exist = os.path.isdir(DirName_new)

        #if (exist == True):
        try:
            os.mkdir(DirName_new)

            files_to_copy = os.listdir(DirName)

            for fname in files_to_copy:
                name,ext = os.path.splitext(fname)
                if(ext == extension):
                    src_fpath = os.path.join(DirName, fname)
                    dst_fpath = os.path.join(DirName_new, fname)

                    if os.path.isfile(src_fpath):
                        shutil.copy(src_fpath, dst_fpath)
                        print(f"Copied: {fname} to {DirName_new}")

        except FileExistsError :
            print("Directory Already exists.")

        except Exception as e:
            print("Exception has occured : ",e)
            

def main():
    print("--------------Automation Script--------------")

    print("Automation Script name : ",argv[0])

    if(len(argv) != 4):
        print("invalid no of arguments")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):     # Flag for displaying help
        print("This automation script is used to display all the files of a given extension present inside a given directory")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):     # Flag for displaying usage of script
        print("Usage : Name_of_the_Script Frist_argument Second_argument")
        exit()
    try:
        DirectoryCopy(argv[1], argv[2], argv[3])
    
    except ValueError : 
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)
    
if __name__ == "__main__":
    main()