import sys
sys.setrecursionlimit(10**6)
n = int(input())

def factorial(x):
    if x == 0 : 
        return 1 
    else:
        return x*factorial(x-1)
print(factorial(n))