prime_count = 0
comp_count = 0
n = int(input("Enter the number :"))
while(n!=-1):
    flag = 0
    for i in range(2,n):
        if(n % i ==0):
            flag = 1
            break
    if(flag == 0):
        prime_count = prime_count+1
    else:
        comp_count = comp_count+1
    n = int(input("Enter the number :"))

print("Number of prime number is :", prime_count)
print("Number of composite number is :",comp_count)