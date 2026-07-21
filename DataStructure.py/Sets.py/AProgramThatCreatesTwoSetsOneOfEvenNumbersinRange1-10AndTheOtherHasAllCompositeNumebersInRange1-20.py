evens = set([x*2 for x in range(1, 10)])
print("EVENS : ", evens)
composites = set()
for i in range(2, 20):
    j = 2
    flag = 0
    while j<=i/2:
        if i % j == 0:
            composites.add(i)
        j+=1
print("COMPOSITES : ", composites)
print("SUPERSET : ", evens.issuperset(composites))
print("ALL : ", all(evens))
print("LENGTH OF COMPOSITES SET : ", len(composites))
print("SUM OF ALL NUMBERS IN EVENS SET : ", sum(evens))