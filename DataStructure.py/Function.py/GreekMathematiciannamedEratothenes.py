def SieveofEratosthenes(n):
    prime = [True for i in range(n + 1)]
    num = 2
    while(num*num <=n):
        if(prime[num] == True):
            for i in range(num ** 2, n + 1, num):
                prime[i] = False
        num +=1
    prime[0] = False
    prime[1] = False
    for num in range(n + 1):
        if prime[num]:
            print(num, end = " ")
n = 50
print("Prime numbers smaller than ", n, " are : ")
SieveofEratosthenes(n)