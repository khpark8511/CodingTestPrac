def solution(players, callings):
    res_key = dict()
    res_value = dict() 
    
    for idx,i  in enumerate(players):
        res_key[i] = idx
        res_value[idx] = i 
    
    for i  in callings:
        pos = res_key[i]
        res_key[i] = pos-1 
        res_key[res_value[pos-1]] = pos

        res_value[pos] = res_value[pos-1]
        res_value[pos-1] = i
    return list(res_value.values())