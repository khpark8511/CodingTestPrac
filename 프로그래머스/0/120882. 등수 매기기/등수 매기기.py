def solution(score):
    idx,res = 0,[]
    # 평균먼저 
    res = sorted([[i+1,sum(score[i])/2] for i in range(len(score))],key=lambda i:-i[1])
    print(res)
    for i in range(len(res)):
        res[i].append(i+1)
        if i != 0 :
            if res[i-1][1] == res[i][1] : res[i][2] = res[i-1][2]
    res = sorted(res, key=lambda i : i[0])
    return [i[2] for i in res ]