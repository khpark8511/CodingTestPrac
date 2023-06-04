from collections import deque
t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue 
            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                queue.append((nx,ny))        
    return 1 


for _ in range(t):
    cnt = 0
    m,n,k = map(int,input().split())
    graph = [[0]*m for x in range(n)]

    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 : 
                cnt += bfs(i,j)
    print(cnt)





    






