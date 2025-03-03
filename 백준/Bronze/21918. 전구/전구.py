n,m = map(int,input().split())
num = list(input().split())
for i in range(m):
    a,b,c = map(int,input().split())
    if a == 1 : 
        num[b-1] = str(c) 
    elif a == 2: 
        for j in range(b-1,c):
            if num[j] == '0': 
                num[j] = '1' 
            else : 
                num[j] = '0' 
    elif a== 3: 
        num[b-1:c] = ['0' for x in range(b-1,c)]
    elif a== 4:
        num[b-1:c] = ['1' for x in range(b-1,c)]
print(' '.join(num))