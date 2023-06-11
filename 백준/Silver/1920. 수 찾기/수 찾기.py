n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
arr.sort()
def binSearch(arr,target,start,end):
    while start <= end:
        mid = (start+end) // 2 
        if target == arr[mid]:
            return 1 
        elif target > arr[mid] : 
            start = mid + 1 
        elif target < arr[mid] : 
            end = mid - 1 
    return 0
for i in arr2:
    print(binSearch(arr,i,0,len(arr)-1))