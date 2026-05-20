def CheckEven(no):
    return (no % 2)==0




def main():
    Data=[11,10,15,20,22,27,30]
    
    print("Actual Data is :",Data)
    
    Fdata=list(filter(CheckEven,Data))
    
    print("Data after filter is :",Fdata)

if __name__=="__main__":
    main()