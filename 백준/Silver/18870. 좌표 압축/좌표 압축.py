import sys 
n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
arr2 = sorted(set(arr))
res = dict()
for i in range(len(arr2)):
    res[arr2[i]] = i          
for i in range(len(arr)):
    print(res[arr[i]],end =' ') 