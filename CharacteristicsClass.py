import gc


class Demo:
    # Class Variable
    No1 = 11
    No2 = 10

    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")


print(Demo.No1)
print(Demo.No2)
