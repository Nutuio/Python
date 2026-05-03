import math
total_prime = 0
total_composite = 0

while(1):
    num = int(input("Enter a number :"))
    if(num == 999):
        break
    elif num < 0:
        print("Square root of negative numbers cannot be calculated")
        continue
    else:
        print("Square root of ", num, " = ", math.sqrt(num))