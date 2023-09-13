import os.path

def main():
    print("Enter the name of the file that you want to open : ")
    File_name = input()

    if(os.path.exists(File_name)):
        fobj = open(File_name, "r")
        if(fobj):
            print("File succesfully opened in reading mode")

            Data = fobj.read()
            print("Data from the file is : ",Data)

            fobj.close()
        else:
            print("unable to open the file")
    else:
        print("File does not exists")


if __name__ == "__main__":
    main()