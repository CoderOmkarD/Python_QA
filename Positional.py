def Display(A,B,C,D):
    print(A,B,C,D)
    
def main():
    # Display(10,20)  NOt Allowed --Less Arguments
    # Display(1,2,3,4,5) Not Allowed --Extra Arguments
    Display(10,20,30,40) #Allowed
    
    
if __name__=="__main__":
    main()
    