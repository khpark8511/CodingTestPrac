import sys
input = sys.stdin.readline
t = int(input())
d = [0]*12
d[1] = 1 
d[2] = 2
d[3] = 4
def dp(n):
    if d[n] > 0 or 0< n <= 3: 
        return d[n]
    d[n] = dp(n-1)+dp(n-2)+dp(n-3)
    return d[n]


for _ in range(t):
    n = int(input())
    print(dp(n))