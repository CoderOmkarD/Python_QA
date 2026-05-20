#Pid and PPid display and comparison
import time
import multiprocessing
import os

def SumEven(No):
    
    print("PID of SumEven :",os.getpid())# 51
    print("PPID of SumEven :",os.getppid())#main 21
    Sum=0
    for i in range(2,No+1,2):
        Sum=Sum+i
    
    print("Even Sum is : ",Sum)

def SumOdd(No):
    
    print("PID of SumOdd :",os.getpid())#101
    print("PPID of SumOdd :",os.getppid())#main 21

    Sum=0
    for i in range(1,No+1,2):
        Sum=Sum+i
    
    print("Odd Sum is : ",Sum)


def main():
    start_time=time.time()
    
    print("PID of main :",os.getpid()) #main 21
    print("PPID of main :",os.getppid()) #CMD 11
    
    t1=multiprocessing.Process(target=SumEven,args=(100000000,))
    t2=multiprocessing.Process(target=SumOdd,args=(100000000,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time=time.time()
    print("Time requred is : ",end_time-start_time)
        
if __name__=="__main__":
    main()  
