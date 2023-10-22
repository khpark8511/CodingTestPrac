n,k = map(int,input().split())
res = 0 
f_s = [0]*7 # 학년별 여자
m_s = [0]*7 # 학년별 남자
for i in range(n):
    s,y = map(int,input().split()) # s(성별) : 0(여자),1(남자), y(학년)
    if s == 0 :
        f_s[y] += 1 
    else:
        m_s[y] += 1    

for i in range(1,7):
    if f_s[i] !=0 :
        if f_s[i] % 2 == 0 :
            res += f_s[i]//2
        else:
            res += f_s[i]//2+ f_s[i]%2
    if m_s[i] !=0 : 
        if m_s[i] % 2 == 0 :
            res += m_s[i]//2
        else:
            res += m_s[i]//2+ m_s[i]%2
print(res)



