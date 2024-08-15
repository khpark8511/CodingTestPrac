res = 0 
num={'ABC':2,'DEF':3,'GHI':4,'JKL':5,'MNO':6,'PQRS':7,'TUV':8,'WXYZ':9}
s = list(input())
for j in s : 
    for i in num.keys():
        if j in i:
            res += (num[i]+1)
            break
print(res)