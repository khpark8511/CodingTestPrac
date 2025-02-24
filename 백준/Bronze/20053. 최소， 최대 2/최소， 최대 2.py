t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    print(min(li),max(li))