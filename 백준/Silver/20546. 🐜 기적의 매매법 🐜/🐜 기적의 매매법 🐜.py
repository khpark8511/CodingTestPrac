def sol():
    m = int(input())
    daily = list(map(int,input().split()))
    p1,p2 = 0,0
    p1_m,p2_m=m,m
    up,down = 0,0
    for i in range(len(daily)):
        if p1_m >= daily[i] : 
            p1 += p1_m//daily[i]
            p1_m = p1_m%daily[i]

        if i > 0 : 
            if daily[i] < daily[i-1]: 
                down += 1 
                up = 0 
            elif daily[i] > daily[i-1] : 
                up += 1 
                down = 0 

            if down >= 3 and p2_m > daily[i] : 
                p2 += p2_m//daily[i]
                p2_m = p2_m%daily[i]
                up = 0 
            elif up >= 3 : 
                p2_m += daily[i]*p2
                p2  = 0
                down = 0 
    res1 = p1_m+daily[-1]*p1
    res2 = p2_m+daily[-1]*p2  
    if res1 > res2 : print("BNP")
    elif res1 == res2 : print("SAMESAME")
    else: print("TIMING")

sol()        
