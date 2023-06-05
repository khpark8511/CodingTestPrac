res = [] 
for i in range(5):
    res.append(int(input()))
res.sort()
print(int(sum(res)/len(res)))
print(res[len(res)//2])
