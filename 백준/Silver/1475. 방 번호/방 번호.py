n = list(map(int,input()))
#print(n)
nset = [0] * 10 
for i in n:
    if i == 6 and nset[i] !=0 and nset[9] < nset[i]  : 
        nset[9] += 1 
    elif i == 9 and nset[i] !=0 and nset[6] < nset[i]:
        nset[6] += 1 
    else:
        nset[i] += 1
#print(nset)
print(max(nset))
