
def Summation(Arr):
    sum=0
    
    for i in range(len(Arr)):
        
        sum=sum+Arr[i]
        
    return sum


def main():
    size=0
    Value=0
    Ret=0
    
    print("Enter the Number Of Element:")
    size=int(input())
    
    Data=list()

    print("Enter the ",size," Elements")
    for i in range(size):
        Value=int(input())
        Data.append(Value)
        
    Ret=Summation(Data)
    print("Summation is : ",Ret )


if __name__=="__main__":
    main()