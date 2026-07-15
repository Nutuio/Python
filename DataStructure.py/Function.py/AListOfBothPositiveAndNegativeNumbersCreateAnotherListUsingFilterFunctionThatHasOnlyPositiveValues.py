def is_positive(x):
    if x>=0:
        return x
num_list = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]
List = []
List = list(filter(is_positive, num_list))
print("positive Values List = ", List)