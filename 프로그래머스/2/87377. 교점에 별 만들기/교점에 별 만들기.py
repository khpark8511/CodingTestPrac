def solution(line):
    res = []
    x_min,x_max,y_min,y_max = 1e15,-1e15,1e15,-1e15
    for i in range(len(line)):
        a,b,e = line[i]
        for j in line[i+1:]:
            c,d,f = j
            if a*d == b*c : continue
            else:
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
                if x == int(x) and y == int(y) : 
                    x = int(x)
                    y = int(y)
                    res.append([x,y])
                    if x_min > x  : x_min = x 
                    if x_max <=x  : x_max = x 
                    if y_min > y  : y_min = y 
                    if y_max <=y  : y_max = y 
    w = abs(x_max-x_min)+1
    h = abs(y_max-y_min)+1
    coord = [['.']*w for _ in range(h)]
    for x,y in res : 
        nx = x + abs(x_min) if x_min < 0 else  x - x_min
        ny = y + abs(y_min) if y_min < 0 else  y - y_min
        coord[ny][nx] = '*'
    res = [] 
    for i in coord:
        res.append(''.join(i))
    return res[::-1]