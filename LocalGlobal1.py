no=11            #Global

def fun():
    no=21        #local
    print("Value of no from Fun is: ",no) #21
    
print("Value of no is: ",no) #11
    
fun()
