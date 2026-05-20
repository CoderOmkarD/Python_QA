def EmployeeInfo(Name,Age,Salary,City):
    print("Name :",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)
    
def main():
    
    # Positional
    # EmployeeInfo("Omkar",24,2000.50,"Pune")#Correct
    # EmployeeInfo(24,"Omkar","Pune",2000.50)#Incorrect
    
    #Keyword
    EmployeeInfo(Age=24,Name="Omkar",City="Pune",Salary=2000.50)        #Correctttt
    
if __name__=="__main__":
    main()  
