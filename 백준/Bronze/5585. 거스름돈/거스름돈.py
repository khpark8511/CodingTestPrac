n = int(input())
n = 1000 - n 
std = [ 500, 100, 50,10,5,1]
cnt = 0 

for i in std : 
    if n >= i : 
        cnt +=  n//i 
        n %= i 
    else:
        continue 
print(cnt)

