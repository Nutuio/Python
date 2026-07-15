def circulate(L, n):
    print("Circulating the elements of list :")
    for i in range(0,n):
        val = L.pop(0)
        L.append(val)
        print(L)
n = int(input("Enter number of values :"))
L = []
for i in range(0,n):
    val = int(input("Enter a value : "))
    L.append(val)
circulate(L,n)