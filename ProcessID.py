import os

def main():
    print("PID of running process is :",os.getpid())
    print("PID of parent process is :",os.getppid())
    
    print("Current Working Directory is :",os.getcwd())
    

if __name__=="__main__":
    main()