import psutil
import os
import time
from sys import *

def ProcessDisplay(log_dir):

    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir, "MarvellousLog_%s_.log" %(time.ctime()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process Logger : "+time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms  = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo);
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
      f.write("%s\n" % element)

    print("Log file is successfully generated at location %s"%(log_path))


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
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid datatype of arguments")
               
    except Exception as e:
        print("Error : invalid input",e)

    print("Log file created succesfully")
if __name__ == "__main__":
    main()