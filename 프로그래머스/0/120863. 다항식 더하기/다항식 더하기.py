def solution(p):
    r1,r2 = 0,0
    res = ''
    p = [_.strip() if _.strip() != 'x' else _.strip().replace('x','1x') for _ in p.split('+')]
    for i in p : 
        if 'x' in i: r1 += int(i[:-1])
        else: r2 += int(i)
    if r1 == 0 : res =str(r2) 
    elif r1 == 1 :
        if r2 == 0 : res= 'x'
        else : res= 'x + '+str(r2)        
    else: 
        if r2 != 0 : res= str(r1)+'x + ' +str(r2)
        else: res = str(r1)+'x'
    print(res)
    return res
            
        