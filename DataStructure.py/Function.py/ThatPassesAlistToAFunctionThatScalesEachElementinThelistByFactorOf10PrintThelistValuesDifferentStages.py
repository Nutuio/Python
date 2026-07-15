def change(list1):
    for i in range(len(list1)):
        list1[i] = list1[i] * 10
    print("After change in function, List is : ", list1)
num_list = [1, 2, 3, 4, 5, 6]
print("Original List is : ", num_list)
change(num_list)
print("List after change is : ", num_list)