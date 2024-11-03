# 11275. 트리의 부모 찾기 
from collections import deque
n = int(input())
graph =[[] for _ in range(n+1)]
parents =[0]*(n+1)
q = deque()

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    q.append(x)
    while q : 
        v = q.popleft()
        for i in graph[v]:
            if not parents[i]:
                parents[i] = v 
                q.append(i)
bfs(1)
for i in range(2,n+1):
    print(parents[i])