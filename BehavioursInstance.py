class Demo:
    No = 10

    def __init__(self, A, B):

        self.Value1 = A
        self.Value2 = B

    def fun(self):
        print("Inside Instance method fun", self.Value1, self.Value2)

    @classmethod
    def Sun(cls):
        print("Inside class Method Sun",cls.No)


Demo.Sun()
print("Class variable no :", Demo.No)

obj = Demo(11, 21)

obj.fun()
print("Instance Variable of obj :", obj.Value1, obj.Value2)
