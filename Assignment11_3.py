import hashlib
import psutil
import os
import time
from sys import *

def hashfile(path, blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")

def ProcessDisplay(log_dir, dict1):

    flag = os.path.isabs(log_dir)

    if flag == False:
        log_dir = os.path.abspath(log_dir)
    
    exists = os.path.isdir(log_dir)

    separator = "-" * 80
    log_filename = "MarvellousLog_%s_.log" % (time.ctime())
    log_filename = log_filename.replace(" ", "_").replace(":", "_")
    log_path = os.path.join(log_dir, log_filename)
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process Logger : "+time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates Found:")
        
        icnt = 0

        for result in results :
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    f.write("%s\n" % subresult)
                    os.remove(subresult)
            icnt = 0


    print("Log file is successfully generated at location %s"%(log_dir))


def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")

    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This Script is used to log recoe=rd of running processes")
        exit()

    if((argv[1] == "-u") or(argv[1] == "-U")):
        print("usage : ApplicationName AbsoultePath_of_Directory")
        exit

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        ProcessDisplay(argv[1], arr)

    except ValueError:
        print("Error : Invalid datatype of arguments")
               
    except Exception as e:
        print("Error : invalid input",e)

    print("Log file created succesfully")
if __name__ == "__main__":
    main()