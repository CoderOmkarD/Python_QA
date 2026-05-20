from functools import reduce

CheckEven=lambda no :no%2==0
Increment=lambda no:no+1
Add=lambda A,B:A+B

def main():
    
    Data=[11,10,15,20,22,27,30]
    print("Actual Data is :",Data)

    Fdata=list(filter(CheckEven,Data))
    print("Data after filter is :",Fdata)

    Mdata=list(map(Increment,Fdata))
    print("Data After map is :",Mdata)

    Rdata=reduce(Add,Mdata)
    print("Data after reduce is :",Rdata)
    
if __name__=="__main__":
    main()