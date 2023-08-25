import functools

def Prime(No):
    Cnt = 0
    for i in range(2,No,1):
        if(No % i == 0):
            Cnt += 1        
    if(Cnt == 0):
        return True
    else:
        return False

Mult = lambda No : No * 2

def Max(No1, No2):
    max = No1
    if (max < No2):
        max = No2
    return max

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
    for no in Elements:
        Ret = Task(Elements[0],no)
    return Ret

def main():
    Size = int(input("Enter the size of the list : "))

    Arr = []

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    print("Input Data is : ",Arr)

    f_output = list(Filter(Prime, Arr))
    print("output after filter : ",f_output)

    m_output = list(Map(Mult,f_output))
    print("Output after MapX : ",m_output)

    result = Reduce(Max,m_output)
    print("Output after reduce : ",result)


if __name__ == "__main__":
    main()