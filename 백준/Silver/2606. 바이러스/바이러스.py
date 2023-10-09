n = int(input())
m = int(input())
graph = [[] for x in range(n+1)]
visited = [0]*(n+1)

global cnt 
cnt = 0 
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def dfs(x):
    global cnt
    visited[x] = True
    for i in graph[x]:
        if not visited[i] : 
            dfs(i)            
            cnt += 1 
    return cnt

print(dfs(1))
