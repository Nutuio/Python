def add(x, y):
    return x + y
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = list(map(add, list1, list2))
print("Sum of ", list1, " and ", list2, " = ", list3)