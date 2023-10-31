import sys 
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
tot,res = 0,0 

arr.sort()
start = 0
end = max(arr)

def bin_srh(arr,target,start,end):
    global res 
    while start <= end : 
        tot = 0 
        mid = (start + end ) // 2 
        for x in arr:
            if x > mid :
                tot += (x-mid)
        if tot >= target :
            res = max(mid,res)
            start = mid + 1   
        else : 
            end = mid - 1 
    return res
print(bin_srh(arr,m,start,end))
             