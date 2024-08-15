p,r,s = '','',''
t = int(input())
for i in range(t) : 
    r,s = input().split()
    r = int(r)
    for j in range(len(s)):
        p += s[j]*r
    print(p)
    p = '' 