def main():
    
    Ans=0
    try:
        print("Inside try")
    
        print("Enter first Number : ")
        no1=int(input())

        print("Enter second Number : ")
        no2=int(input())

        Ans=no1/no2
          
    except:
        print("Inside except")
        
    finally:
        print("Inside Finally")
        
    print("Division is : ",Ans)    

if __name__=="__main__":
    main()