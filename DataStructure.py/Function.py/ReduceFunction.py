import functools
def add(x, y):
    return x + y
num_list = [1, 2, 3, 4, 5]
print("Sum of values in list = ")
print(functools.reduce(add, num_list))