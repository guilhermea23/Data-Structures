import math
def fact(n):
    if n < 2:
        return 1
    else:
        fact = n * math.factorial(n-1)
        return fact

n = int(input())
print(fact(n))