n = int(input())
res = 0 
data = list(map(int,input().split()))
data.sort()
for i in range(n): # 0 ~ n-1
    res += (n-i)*data[i]
print(res)