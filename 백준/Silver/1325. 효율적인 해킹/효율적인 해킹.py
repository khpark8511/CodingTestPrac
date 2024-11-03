# 1325. 효율적인 해킹 
import sys 
from collections import deque 
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
q = deque()
res, max_i,max_val =0,[],[0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

def bfs(x):
    global res 
    visited[x] = True
    q.append(x)
    while q : 
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                res += 1 
                q.append(i)

for i in range(1,n+1):
    res = 0  
    visited = [0]*(n+1)
    bfs(i)
    max_val[i] = res 
for i in range(1,n+1):    
    if max(max_val) == max_val[i] : 
        max_i.append(i)
print(*max_i)