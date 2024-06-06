def solution(numer1, denom1, numer2, denom2):
    res = [] 
    a,b,c,d = numer1, denom1, numer2, denom2
    if (a*d+b*c)%(b*d) == 0 :
        return [(a*d+b*c)//(b*d),1]
    elif (b*d)%(a*d+b*c)==0 : 
        return [1,(b*d)//(a*d+b*c)]
    elif (a*d+b*c) > (b*d)  : 
        for i in range(b*d,1,-1):
            if (a*d+b*c)%i == 0 and (b*d)%i == 0 : 
                return [(a*d+b*c)//i,(b*d)//i]
        return [a*d+b*c,b*d]
    else:
        for i in range((a*d+b*c),1,-1):
            if (a*d+b*c)%i == 0 and (b*d)%i == 0 : 
                return [(a*d+b*c)//i,(b*d)//i]
        return [a*d+b*c,b*d]