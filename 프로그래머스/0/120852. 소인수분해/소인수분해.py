def solution(n):
    res = set()
    i = 2
    while i < n+1:
        if n not in res and n%i == 0 : 
            n //= i 
            res.add(i)
            i = 2
        i += 1 
    res2 = res.copy()
    for i in res2 : 
        for j in range(2,i+1):
            if i!=j and i%j==0:
                res.remove(i)
                break
    return sorted(list(res))
            