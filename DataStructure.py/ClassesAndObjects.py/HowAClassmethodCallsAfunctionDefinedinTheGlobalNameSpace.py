def scale_10(x):
    return x*10
class ABC():
    def __init__(self, var):
        self.var = var
    def display(self):
        print("Var is = ", self.var)
    def modify(self):
        self.var = scale_10(self.var)
obj = ABC(10)
obj.display()
obj.modify()
obj.display()