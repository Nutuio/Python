import functools
def max_ele(x, y):
    return x >  y
num_list = [4, 1, 8, 2, 9, 3, 0]
print("Largest value in the list is : ", functools.reduce(max, num_list))