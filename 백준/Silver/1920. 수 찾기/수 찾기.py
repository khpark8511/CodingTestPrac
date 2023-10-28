n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
arr.sort()

def bin_srh(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start =mid+1
    return None

for x in arr2:
    res = bin_srh(arr,x,0,n-1)
    if res != None:
        print(1)
    else:
        print(0)