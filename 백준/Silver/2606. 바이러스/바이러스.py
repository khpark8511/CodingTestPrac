import sys 

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for x in range(n+1)]
visited = [0]*(n+1)
global cnt 
cnt = 0 

def dfs(x):
    global cnt 
    if not visited[x] :
        visited[x] = 1
        cnt += 1 
        for i in graph[x] : 
            if not visited[i] : 
                dfs(i)
    return cnt 

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(1)-1)
