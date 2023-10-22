import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    tmp = input().rstrip() # 문자열 
    l = []    # 커서 왼쪽
    r = []    # 커서 오른쪽 
    for j in tmp:
        if j == '<':
            if l : # 커서 왼쪽에 문자열이 있을 경우
                r.append(l.pop())
        elif j == '>' :  
            if r: # 커서 오른쪽에 문자열이 있을 경우
                l.append(r.pop())
        elif j == '-':
            if l : 
                l.pop()
        else:
            l.append(j)
    l.extend(reversed(r))
    print(''.join(l))




