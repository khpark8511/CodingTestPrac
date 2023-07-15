def solution(park, routes):
    global row, col
    row = len(park)
    col = len(park[0])
    
    dx = 0
    dy = 0 
    x , y = -1 ,0 
        
    for i in park:
        x += 1
        if 'S' in i : 
            y = i.index('S')
            print(x,y)
            break
                
    for i in routes:        
        tmpx, tmpy = dfs(i,park,x,y)
        if tmpx == -1 and tmpy == -1 :
            continue
        else:
            x,y = tmpx,tmpy
    return [x,y]
            
    
    
def dfs(i,park,x,y):
    global row,col 
    str_i = ' '.join(i)
    dir = str(str_i[0])
    num = int(str_i[-1])
    if dir == 'E':
        dx = x 
        dy = y + num
    elif dir == 'W':
        dx = x 
        dy = y - num  
    elif dir == 'N':
        dx = x - num
        dy = y
    elif dir == 'S':
        dx = x + num
        dy = y
    if dx < 0 or dy < 0 or dx >= row or dy >= col:
        return (-1,-1)     
    
    if dir == 'S' or dir == 'N':
        if x >= dx:  
            for i in range(dx,x+1):
                if park[i][dy] == 'X':
                    return (-1,-1)
        else:
            for i in range(x,dx+1):
                if park[i][dy] == 'X':
                    return (-1,-1)
    elif dir == 'E' or dir == 'W':  
        if y >= dy:
            for i in range(dy,y+1):
                if park[dx][i] == 'X':
                    return (-1,-1)  
        else:
            for i in range(y,dy+1):
                if park[dx][i] == 'X':
                    return (-1,-1)  
    x,y = dx,dy
    return (x,y)

            