import sys
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ('x', 'y')
obj1 = WithoutSlots(10, 20)
obj2 = WithSlots()
obj2.x = 10
obj2.y = 20

print(f"Memory (Without __slots__):{sys.getsizeof(obj1.__dict__)}bytes",obj1.__dict__)
print(f"Memory (With __slots__):{sys.getsizeof(obj2.__slots__)}bytes",obj2.__slots__)


print("without slots : ", obj1.x,obj1.y)
print("with slots : ", obj2.x,obj2.y)