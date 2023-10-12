from collections import deque
n = int(input())
global res,y
x,y = map(int,input().split())
m = int(input())
graph =  [[] for x in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i] : 
                visited[i] = visited[v]+1
                queue.append(i)
            if i == y :
                return visited[i]
    return -1

print(bfs(x))