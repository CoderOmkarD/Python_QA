from functools import reduce

def main():
    
    Data=[11,10,15,20,22,27,30]
    print("Actual Data is :",Data)

    Fdata=list(filter((lambda no : no %2 ==0),Data))
    print("Data after filter is :",Fdata)

    Mdata=list(map((lambda no : no+1 ),Fdata))
    print("Data After map is :",Mdata)

    Rdata=reduce(lambda A,B : A + B,Mdata)
    print("Data after reduce is :",Rdata)
    
if __name__=="__main__":
    main()
