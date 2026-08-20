class ABC():
    def __init__(self,val):
        print("IN class method....")
        self.val = val
        print("The value is : ", val)
obj = ABC(10)