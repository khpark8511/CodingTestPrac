def solution(n):
    board = [[0]*n for _ in range(n)]
    dir = [(-1,1),(1,0),(0,-1)] # <, > , ^  
    ny,nx = 0,0
    nsum = sum([i for i in range(1,n+1)])
    diridx,idx = 0,1
    y,x = 0,n-1 
    board[y][x] = 1
    
    while True : 
        px,py = dir[diridx]
        while 0<= x+px < n and 0<= y+py < n :
            if board[y+py][x+px] == 0 :
                x = x + px
                y = y + py
                idx += 1  
                board[y][x] = idx
            else: break
        if idx == nsum : 
            return [j for i in board for j in i if j != 0 ]
        else : 
            if diridx == 2 : diridx = 0 
            else: diridx += 1 