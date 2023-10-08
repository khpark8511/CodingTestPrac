from collections import deque
#dfs
def dfs_func(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]: 
            dfs_func(graph,i,visited)

#bfs
def bfs_func(graph,start,visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v=  queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




n,m,v = map(int, input().split())
graph = [[] for i in range(n+1)]

visited = [False] * (n+1)
graph.append([])
for i in range(1,m+1):
    first, second = map(int,input().split())    
    if first >= 0 and first <= n:
        graph[first].append(second)
        graph[first].sort()
    if second >= 0 and second <= n:
        graph[second].append(first)
        graph[second].sort()    
    
dfs_func(graph,v,visited)
visited = [False] * (n+1)
print()
bfs_func(graph,v,visited)
