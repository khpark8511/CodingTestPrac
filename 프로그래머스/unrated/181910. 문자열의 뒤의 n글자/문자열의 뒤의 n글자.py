def solution(my_string, n):
    res = ''
    for i in range(-n,0):
        res += my_string[i]
    return res