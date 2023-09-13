import os.path
import shutil

def main():
    print("Enter the name of the file that you want to create : ")
    File_name = input()

    if(os.path.exists(File_name)):
        print("File already exists")            
    else:
        fobj = open(File_name, "x")
        
        print("Enter the name of the file to copy the contents")
        File1_name = input()

        source_file= open(File1_name, 'rb')
        destination_file = open(File_name, 'wb')

        shutil.copyfileobj(source_file, destination_file)

if __name__ == "__main__":
    main()