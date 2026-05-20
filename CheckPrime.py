def CheckPrime(iNo):
    i=2
    bflag=False
    for i in range(1,int((iNo/2))+1):
        if iNo%i!=0:
            bflag=True
        elif iNo%i==0:
            bflag=False
        
    return bflag

print("Enter the Number to check Prime:")
iValue=int(input())

Result=CheckPrime(iValue)

if Result==False:
    print("It is a Not Prime Number")
else:
    print("It is a Prime NUmber")