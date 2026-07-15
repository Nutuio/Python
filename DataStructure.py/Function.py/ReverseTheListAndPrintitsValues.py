num_list = []
m = int(input("Enter the staring of the range : "))
n = int(input("Enter the ending of the range : "))
o = int(input("Enter the steps in the range : "))
for i in range(m,n, o):
    num_list.append(i)
print("Original list : ", num_list)
num_list.reverse()
print("Reversed List : ", num_list)