def solution(s):
    s = s.lower()
    res = [] 
    res.append(s.count('p'))
    res.append(s.count('y'))
    if res[0] == 0 and res[1] == 0: 
        return True
    elif res[0] == res[1]:
        return True
    else:
        return False