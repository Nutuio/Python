def to_lower(str):
    return str.lower()
list1 = ["HELLO", "WELCOME", "TO", "PYTHON"]
list2 = list(map(to_lower, list1))
print("List in lowercase characters is : ", list2)