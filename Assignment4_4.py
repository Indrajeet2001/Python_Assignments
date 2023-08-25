import functools

Check = lambda No : (No % 2 == 0)

Square = lambda No : No * No

Add = lambda A,B : A + B

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
    Sum = 0
    for no in Elements:
        Sum = Task(Sum,no)
    #    Ret = Task(Ret, no)
    #   Sum = Ret
    return Sum

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

    m_output = list(Map(Square,f_output))
    print("Output after MapX : ",m_output)

    result = Reduce(Add,m_output)
    print("Output after reduce : ",result)


if __name__ == "__main__":
    main()