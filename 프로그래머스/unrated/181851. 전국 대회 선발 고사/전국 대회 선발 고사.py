def solution(rank, attendance):
    att = [] 
    for i in range(len(rank)):
        if attendance[i]:
            att.append([i,rank[i]])
            
    att.sort(key = lambda x : x[1])
    print(att)
    
    a = int(att[0][0])
    b = int(att[1][0])
    c = int(att[2][0])
    
    return 10000*a+100*b+c    