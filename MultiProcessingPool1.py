def SumCube(no):
    Sum=0
    
    for i in range(1,no+1,1):
        Sum=Sum+(i*i*i)
        
    return Sum

def main():
    
   
    Ret=SumCube(10)
    
    print(Ret)
    
if __name__=="__main__":
    main()