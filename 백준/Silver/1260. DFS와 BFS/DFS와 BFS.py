from collections import deque 
n,m,v = map(int,input().split())
q = deque()
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

def dfs(x):
    if not visited[x]:
        visited[x] = True
        print(x, end =' ')
        for i in graph[x]:
            if not visited[i]:
                dfs(i)
def bfs(x):
    print(x,end=' ')
    visited[x] = True
    q.append(x)
    while q : 
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                print(i,end=' ')
dfs(v)
print()
visited = [0]*(n+1)
bfs(v)
                