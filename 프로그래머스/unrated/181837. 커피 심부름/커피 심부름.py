def solution(order):
    res = 0 
    for i in order:
        if 'americano' in i :
            res += 4500
        elif 'latte' in i :
            res += 5000
        else:
            res += 4500
    return res