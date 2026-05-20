from functools import reduce

def CheckEven(no):
    return (no % 2)==0

def Increment(no):
    return no+1

def Add(A,B):
    return A+B

def main():
    
    Data=[11,10,15,20,22,27,30]
    ##############################
    print("Actual Data is :",Data)
    
    
    ##############################
    Fdata=list(filter(CheckEven,Data))
    
    print("Data after filter is :",Fdata)
    
    
    ###############################
    Mdata=list(map(Increment,Fdata))
    
    print("Data After map is :",Mdata)
        
    ################################
    
    Rdata=reduce(Add,Mdata)
    
    print("Data after reduce is :",Rdata)
    
    

if __name__=="__main__":
    main()