class ABC():
    def __init__(self, var):
        self.var = var
    def display(self):
        print("Var is = ", self.var)
obj = ABC(10)
obj.display()
obj.new_var = 20
print("New Var = ", obj.new_var)
obj.new_var = 30
print("New Var after modification = ", obj.new_var)
del obj.new_var
print("New Var after deletion = ", obj.new_var)