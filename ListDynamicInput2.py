def main():
    size=0
    print("Enter the Number Of Element:")
    size=int(input())
    Value=0
    
    Data=list()
    
    # Data[0]=11 Errorrrrrrrrr

    print("Enter the ",size," Elements")
    for i in range(size):
        Value=int(input())
        Data.append(Value)
        
    sum=0
    
    for i in range(size):
        sum=sum+Data[i]
    print("Summation is : ",sum )

if __name__=="__main__":
    main()