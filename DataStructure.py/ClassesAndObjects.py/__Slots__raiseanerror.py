class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class WithSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
point = WithoutSlots(1, 2)
point.z = 3
point = WithSlots(1, 2)
try:
    point.z = 3
except AttributeError as e:
    print("raised Attribute Error",e)
