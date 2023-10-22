n,k = map(int,input().split())
li = [i for i in range(1,n+1)]
res = [] 
idx = 0 

for i in range(n):  
    idx += k-1
    if idx >= len(li):
        idx = idx%len(li)
    res.append(str(li.pop(idx)))
print('<',', '.join(res),'>',sep='') 
