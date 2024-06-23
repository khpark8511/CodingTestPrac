def solution(rows, columns, queries):
    minli = [] 
    coord = [[(columns*j)+i for i in range(1,columns+1)] for j in range(rows)]
    for y1,x1,y2,x2 in queries : 
        tmp,minnum = 0, 1e15
        y1 -= 1 
        x1 -= 1 
        y2 -= 1 
        x2 -= 1 
        tmp = coord[y1][x1] 
        for i in range(y1+1,y2+1):
            coord[i-1][x1] = coord[i][x1]
            if minnum > coord[i][x1] : minnum = coord[i][x1]
        for i in range(x1+1,x2+1):
            coord[y2][i-1] = coord[y2][i]
            if minnum > coord[y2][i] : minnum = coord[y2][i]
        for i in range(y2-1,y1-1,-1):
            coord[i+1][x2] = coord[i][x2]
            if minnum > coord[i][x2] : minnum = coord[i][x2]
        for i in range(x2-1,x1,-1):
            coord[y1][i+1] = coord[y1][i]
            if minnum > coord[y1][i] : minnum = coord[y1][i]
        coord[y1][x1+1] = tmp 
        if minnum > tmp : minnum = tmp
        minli.append(minnum)
    return minli
