num = 1 
numlist = [0]*10
for i in range(3):
    num *= int(input())
res = list(map(int,str(num)))

for i in res:
    numlist[i] += 1 
for i in range(len(numlist)):
    print(numlist[i])



