n = int(input())
d = {1:1, 2:2}

def dp(n):
    if n ==1 or n==2:
        return d[n] 
    
    elif n not in d : 
        d[n] = (dp(n-1)+dp(n-2))%10007
    return d[n] 

print(dp(n))