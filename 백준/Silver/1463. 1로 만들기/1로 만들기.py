import sys
input = sys.stdin.readline
n = int(input())
d = {1:0, 2:1, 3:1}
def dp(n):
    if n in d :
        return d[n]
    cnt = min(dp(n//3)+n%3,dp(n//2)+n%2)+1
    d[n] = cnt
    return cnt
 
print(dp(n))