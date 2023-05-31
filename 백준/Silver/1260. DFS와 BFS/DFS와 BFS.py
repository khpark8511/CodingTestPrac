from collections import deque

n,m,v = map(int,input().split())
graph = [[] for x in range(n+1)]
visited = [False]*(n+1) 
for i in range(m):
    first, second = map(int,input().split())
    graph[first].append(second)
    graph[second].append(first)
    graph[first].sort()
    graph[second].sort()

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):  
    queue = deque([start])
    visited[start] = True  
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



dfs(graph,v,visited)
visited = [False]*(n+1) 
print()
bfs(graph,v,visited)
        
