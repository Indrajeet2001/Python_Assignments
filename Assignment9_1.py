import os.path

def main():
    print("Enter the name of the file that you want to check : ")
    File_name = input()

    if(os.path.exists(File_name)):
        print("File Exists...")
    else:
        print("File does not exists")


if __name__ == "__main__":
    main()