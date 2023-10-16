n = int(input())
num = list(map(int,input().split()))
m = int(input())
cnt = 0 

for i in range(len(num)):
    if m == num[i] : 
        cnt += 1
print(cnt) 