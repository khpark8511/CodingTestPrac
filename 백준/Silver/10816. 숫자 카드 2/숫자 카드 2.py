import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
arr2 = list(map(int,sys.stdin.readline().split()))

arr_dst = set(arr) 
chk = dict()
for i in range(len(arr_dst)):
    k = arr_dst.pop()
    chk[k] = 0
#print(chk)
    
for i in arr:
    if i in chk.keys():
        chk[i] += 1 
#print(chk)

for i in arr2:
    if i in chk.keys():
        print(chk[i], end = ' ')
    else:
        print(0, end=' ')