import time

def Factorial(No):
    Fact=1
    for i in range(1,No+1):
        Fact=Fact*i
        
    return Fact

def main():
    
    
    Value=int(input("Enter the Number: "))
    
    
    Start_Time=time.time()
    print("Start Time is : ",Start_Time)
    
    Ret=Factorial(Value)
    
    print("Factorial is : ",Ret)
    
    End_Time=time.time()
    
    print("End time is : ",End_Time)
    
    print("Total Execution time : ",End_Time-Start_Time)

if __name__=="__main__":
    main()