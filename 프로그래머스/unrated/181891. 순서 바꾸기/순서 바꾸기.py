def solution(num_list, n):
    tmp1 = num_list[n:len(num_list)]
    tmp2 = num_list[0:n]
    
    tmp = tmp1+tmp2
    return tmp