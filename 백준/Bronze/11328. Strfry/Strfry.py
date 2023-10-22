n = int(input())
#print(a,b)
#print(la,lb)
for i in range(n):
    a,b = map(str,input().split())
    la = list(a)
    lb = list(b)
    la.sort()
    lb.sort()
    if la == lb : 
        print('Possible')
    else:
        print('Impossible')

