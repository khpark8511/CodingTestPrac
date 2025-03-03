n = int(input())
switch = list(map(int,input().split()))
len_s = len(switch)
s_num = int(input())
for _ in range(s_num):
    a,b = map(int,input().split()) # 성별(남:1, 여:2), 학생이 받은 수 
    if a == 1 : # 남자 
       for i in range(1,len_s//b+1):
           if switch[i*b-1] == 0 : switch[i*b-1] = 1 
           else : switch[i*b-1] = 0  
    else : # 여자 
        for i in range(1,len_s+1):
            l_idx = b-1-i
            r_idx = b-1+i
            if 0<= l_idx < len_s and 0<= r_idx < len_s : # index 내부 
                if switch[l_idx] != switch[r_idx] : # 좌 == 우 
                    if switch[b-1] ==0 : switch[b-1] = 1 # 0 -> 1 
                    else : switch[b-1] = 0 # 1 -> 0 
                    break
                else : # 좌 != 우 
                    if switch[l_idx] == 0 : # 0 -> 1 
                        switch[l_idx] = 1
                        switch[r_idx] = 1
                    else: # 1 -> 0 
                        switch[l_idx] = 0
                        switch[r_idx] = 0
            else: # index out 
                if switch[b-1] ==0 : switch[b-1] = 1
                else : switch[b-1] = 0 
                break
for i in range(0,len_s,20):
    print(*switch[i:i+20])