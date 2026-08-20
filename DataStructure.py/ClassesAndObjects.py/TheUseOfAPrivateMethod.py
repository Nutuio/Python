class ABC():
    def __init__(self, var):
        self.__var = var
    def __display(self):
        print("From class method, Var = ", self.__var)
obj = ABC(10)
obj._ABC__display()