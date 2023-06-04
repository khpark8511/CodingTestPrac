import sys
sys.setrecursionlimit(2501)
# 1012 유기농 배추 > 인접 
t = int(input())

def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0 
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


for _ in range(t):
    res = 0 
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for i in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1 
    
    for l in range(n):
        for j in range(m):
            if dfs(l,j) == True:
                res += 1
    print(res)


    

