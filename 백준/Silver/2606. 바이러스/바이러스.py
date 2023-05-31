#virus 
from collections import deque

com = int(input())
con = int(input())
visited=[False]*(com+1)
graph= [[] for x in range(com+1)]

for i in range(con):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
#print(graph)

def bfs(graph,v,visited):
    cnt = 0
    queue = deque([v])
    visited[v] = True 
    queue.append(v)
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt

print(bfs(graph,1,visited))