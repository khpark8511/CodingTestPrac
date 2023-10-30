import sys 
input = sys.stdin.readline
m,n = map(int,input().split())
arr = list(map(int,input().split()))

start = 1
end = max(arr)
tot,res = 0,0 
arr.sort()

while start <= end : 
    tot = 0
    mid = (start+end) // 2 
    for i in arr : 
        tot +=  i // mid 
    if tot >= m : 
        res = max(res,mid) 
        start = mid + 1 
    else : 
        end = mid - 1
print(res)

