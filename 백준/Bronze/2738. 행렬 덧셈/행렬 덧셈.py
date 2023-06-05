n,m = map(int,input().split())
a = [[] for x in range(n)]
b = [[] for x in range(n)]

for i in range(n):
    a[i] = list(map(int,input().split()))
for j in range(n):
    b[j] = list(map(int,input().split()))
for i in range(n):
    for j in range(m):
        a[i][j] = a[i][j] + b[i][j]
        print(int(a[i][j]), end=' ')
    print()




