import sys
from collections import deque 
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
n = int(input()) 
graph = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [-1,1,0,0] # < , > , ^ , v 
dy = [0,0,-1,1]
res,rg_res = 0,0

def bfs(x,y):
    queue = deque()
    visited[y][x] = 1 
    queue.append((x,y))
    while queue : 
        nx,ny = queue.popleft()
        for i in range(4):
            tmp_x = nx + dx[i]
            tmp_y = ny + dy[i] 
            if 0 <= tmp_x < n and 0<= tmp_y < n and not visited[tmp_y][tmp_x] and graph[tmp_y][tmp_x] == graph[ny][nx] : 
                visited[tmp_y][tmp_x] = 1 
                queue.append((tmp_x,tmp_y))
    return 1 


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            res += bfs(j,i)
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G': 
            graph[i][j] = 'R'
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            rg_res += bfs(j,i)
print(res,rg_res)
