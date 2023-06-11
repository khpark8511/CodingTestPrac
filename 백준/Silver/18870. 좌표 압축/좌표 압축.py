n = int(input())
cnt = 0 
res = dict()
num = list(map(int,input().split()))

zip = sorted(num)
for i in range(n):    
    if i > 0 : 
        if zip[i-1] != zip[i]:
            cnt += 1
    res[zip[i]] = cnt

for i in num:
    print(int(res[i]), end=' ')