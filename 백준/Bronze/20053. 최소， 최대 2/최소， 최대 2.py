n = int(input())
res = []
for i in range(n):
    res = []
    t = int(input())
    num = list(map(int,input().split()))
    res.append(min(num))
    res.append(max(num))
    print(*res)

