class ABC():
    var = 10
    def display(self):
        print("IN class method....")
obj = ABC()
print(obj.var)
obj.display()