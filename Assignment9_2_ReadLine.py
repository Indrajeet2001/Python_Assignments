import os.path

def main():
    print("Enter the name of the file that you want to create : ")
    File_name = input()

    if(os.path.exists(File_name)):
        fobj = open(File_name, "r")
        if(fobj):
            print("File succesfully opened in reading mode")

            print("Data from the file is : ")
            for line in fobj:
                print(line)

            fobj.close()
        else:
            print("unable to open the file")
    else:
        print("File does not exists")


if __name__ == "__main__":
    main()