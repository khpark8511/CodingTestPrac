n = int(input())
num = [0]*11
chk = [0]*11
cnt = 0 
for i in range(n):
    a,b = map(int,input().split())
    if chk[a-1] == 0 : 
        num[a-1] = b 
        chk[a-1] += 1 
    elif num[a-1] != b :
        num[a-1] = b 
        chk[a-1] += 1 
        cnt += 1 
print(cnt)