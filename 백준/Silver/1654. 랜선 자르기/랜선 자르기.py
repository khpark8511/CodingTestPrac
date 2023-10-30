import sys 
input = sys.stdin.readline
k,n = map(int,input().split()) 
arr = [] 
for i in range(k):
    arr.append(int(input()))
arr.sort()


start = 1  
end = max(arr)

while start <= end :
    mid = (start + end ) // 2
    tot = 0 
    for i in arr : 
        tot += i // mid 
    if tot < n : 
        end = mid -1 
    else : 
        res = mid 
        start = mid + 1  
print(res)
