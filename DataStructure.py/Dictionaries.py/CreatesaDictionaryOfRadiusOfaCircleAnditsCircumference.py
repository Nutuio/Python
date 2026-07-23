print("Enter -1 to exit....")
Circumference = {}
while True:
    r = float(input("Enter a Radius :"))
    if r == -1:
        break
    else:
        Dict = {r:2*3.14*r}
        Circumference.update(Dict)
print(Circumference)