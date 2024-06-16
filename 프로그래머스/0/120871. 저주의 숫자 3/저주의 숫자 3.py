def solution(n):
    res = 0 
    for _ in range(n):
        res += 1 
        while '3' in str(res) or res%3 ==0 :
            res += 1 
    return res