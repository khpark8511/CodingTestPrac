import sys 
input = sys.stdin.readline
n,m = map(int,input().split())

a = set(map(int,input().split()))
a_cp = list(a)
a_d = dict()
b = set(map(int,input().split()))

a_cp.sort()
for i in a_cp:
    a_d[i] = 1 

for x in b : 
    if x in a:
        #a_cp.remove(x)
        a_d.pop(x)

print(len(a_d))
if len(a_d) != 0 : 
    print(*list(a_d.keys()))