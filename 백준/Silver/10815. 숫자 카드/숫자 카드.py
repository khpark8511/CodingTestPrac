import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))

def bin_srh(arr,target,start,end):
    while start <= end : 
        mid = (start + end )//2 
        if arr[mid] > target : 
            end = mid -1 
        elif arr[mid] == target : 
            return mid 
        else :
            start = mid + 1 
    return None

arr.sort()
start = 0 
end = n-1
for i in find : 
    res = bin_srh(arr,i,start,end)
    if res != None : 
        print(1, end=' ')
    else:
        print(0, end = ' ')
    