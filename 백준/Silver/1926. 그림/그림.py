from collections import deque
n,m = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
global hcnt
hcnt, res,hmax =0, 0,0 

for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs(a,b):
    global hcnt
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                queue.append((nx,ny))
                hcnt += 1 
            else:
                continue
    return 1 

for i in range(n):
    for j in range(m):
        hcnt = 1
        if graph[i][j]== 1 :
            res += bfs(i,j)
            hmax = max(hmax,hcnt)
         
        else:
            continue
print(res)
print(hmax)