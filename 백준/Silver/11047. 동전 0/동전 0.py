n,k = map(int,input().split())
a = []
res =0
for _ in range(n):
    coin = int(input())
    a.append(coin)
a.sort(reverse=True)

for coin in a:
    if k !=0:
        res += k//coin 
        k %= coin
    else:
        break    
print(res)        
