CheckEven=lambda no :no%2==0
Increment=lambda no:no+1
Add=lambda A,B:A+B

def filterX(Task,Elements):
    
    Result=list()
    
    for no in  Elements:
        Ret=Task(no)
        
        if(Ret==True):
            Result.append(no)
            
    return Result
    
def mapX(Task,Elements):
    
    Result=list()
    
    for no in Elements:
        Ret=Task(no)
        Result.append(Ret)
    
    return Result

def reduceX(Task,Elements):
    Sum=0
  
    for no in Elements:
        Sum=Task(Sum,no)
        
    return Sum
        

def main():
    
    Data=[11,10,15,20,22,27,30]
    print("Actual Data is :",Data)

    Fdata=list(filterX(CheckEven,Data))
    print("Data after filter is :",Fdata)

    Mdata=list(mapX(Increment,Fdata))
    print("Data After map is :",Mdata)

    Rdata=reduceX(Add,Mdata)
    print("Data after reduce is :",Rdata)
    
if __name__=="__main__":
    main()