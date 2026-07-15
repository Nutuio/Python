L = [lambda x: x * 2, lambda x: x * 3, lambda x: x * 4]
for f in L:
    print(f(5))
print("\n Multiplying the value of 100 by 2 we get : ", (L[0](100)))