arr = [-1]*10
tot = 0 
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if arr[a-1] != -1 and arr[a-1] != b : 
        tot += 1 
        arr[a-1] = b 
    elif arr[a-1] == -1 : 
        arr[a-1] = b 
print(tot)
        