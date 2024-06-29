def solution(N, stages):
    cn= {i:0 for i in range(1,N+1)}
    an= {i:0 for i in range(1,N+1)}
    an_cnt = [0]*(N+1)
    tmp = 0 
    res = []
    s = set(stages) 
    while s:
        i = s.pop()
        if i > N : 
            an_cnt[N] += stages.count(i)
            tmp += stages.count(i)
        else: an_cnt[i] = stages.count(i)   
    for i in range(1,N+1):
        an[i] = sum(an_cnt[i:])
        if i < N :
            cn[i] = sum(an_cnt[i+1:])
        else:
            cn[N] = tmp
    res = sorted({i: (an[i]-cn[i])/an[i] if an[i] != 0 else 0 for i in range(1,N+1)}.items(), key= lambda i:(-i[1],i[0]))
    return [i[0] for i in res ]