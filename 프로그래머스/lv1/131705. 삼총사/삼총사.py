from itertools import combinations

def solution(number):
    res = []
    subset = list(combinations(number,3))
    for i in subset:
        dsum = sum(i)
        res.append(dsum)
    
    print(res.count(0))
    return res.count(0)
    
            
        