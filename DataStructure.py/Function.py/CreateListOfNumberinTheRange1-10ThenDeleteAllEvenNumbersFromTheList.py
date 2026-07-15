num_list = []
for i in range(1, 11):
    num_list.append(i)
print("Original List : ", num_list)
for index, i in enumerate(num_list):
    if(i % 2== 0):
        del num_list[index]
print("List after deleting even numbers : ", num_list)