import functools

Increase = lambda No : No + 10

Mult = lambda A,B : A * B

def Check(No):
    if((No >= 70) & (No <= 90)):
        return True
    else:
        return False

def Filter(Task, Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

# Task : Name of function
# Elements : List of data elements
def Map(Task, Elements):
    Result = []
    for no in Elements:
        ret = Task(no)
        Result.append(ret)
    return Result

# Task : Name of function
# Elements : List of data elements
def Reduce(Task, Elements):
    Ret = 1
    for no in Elements:
        Ret = Task(Ret,no)
    #    Ret = Task(Ret, no)
    #   Sum = Ret
    return Ret

def main():
    Size = int(input("Enter the size of the list : "))

    Arr = []

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    print("Input Data is : ",Arr)

    f_output = list(Filter(Check, Arr))
    print("output after filter : ",f_output)

    m_output = list(Map(Increase,f_output))
    print("Output after MapX : ",m_output)

    result = Reduce(Mult,m_output)
    print("Output after reduce : ",result)


if __name__ == "__main__":
    main()