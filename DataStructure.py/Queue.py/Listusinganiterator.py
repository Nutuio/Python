num_list = [1, 2, 3, 4, 5]
it = iter(num_list)
for i in range(len(num_list)):
    print("Element at index ", i, " is :", next(it))