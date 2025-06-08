def solution(babbling):
    std = {'aya','ma','woo','ye'}
    cnt = 0
    for word in babbling :  
        used = set()
        success = True 
        i = 0 
        while i < len(word) : 
            matched = False 
            for s in std :  
                if word[i:i+len(s)] == s and s not in used : 
                    i += len(s)
                    used.add(s)
                    matched = True
                    break 
            if not matched : # 유효하지않은 단어로 구성 
                success = False
                break
        if success : 
            cnt += 1 
    return cnt 
                
                
                    
                    
        
        