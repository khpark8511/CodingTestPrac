def solution(n):
    res = [0 if i != 1 and i !=2 else i for i in range(0,n+1)]
    if n <= 2 : return res[n]
    else:
        for i in range(3,n+1):
            tmp,idx= 1,1 
            while '3' in str(res[i-1]+tmp) or (res[i-1]+tmp)%3 ==0 :
                tmp += 1 
            res[i] = res[i-1]+tmp
    return res[n]