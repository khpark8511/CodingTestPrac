
n = int(input())
m, x, y, cnt, res, minnum = 0,0,0,0,0,-1

while 5*x <= n :
    res = 0 
    m = n 
    m = m - (5*x)

    if m % 3 == 0 : 
        res += x 
        res += m//3 
    else : 
        res = -1 

    if res != -1 :
        if minnum == -1 :  
            minnum = res
        elif minnum > res:
            minnum = res
    elif cnt == 0 :
        minnum = res 
    x += 1
    cnt += 1

print(minnum) 