n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
res,f_res = [],[]
visited = [0]*(n+1)

# 3.stack을 사용해서 bfs check 
def chk(x):
    stack = [] 
    visited[x] = 1 
    stack.append(x)
    while stack : 
        now = stack.pop()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                stack.append(next)
    res.append(sum(visited))   
# 1.노드 연결 정보 입력받기 
for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
# 2.노드 별 연결상태 확인 chk 
for i in range(1,n+1):
    visited = [0]*(n+1)
    chk(i)
# 4.max 값 index 확인 
for i in range(n):
    if max(res) == res[i] : 
        f_res.append(i+1)
print(*f_res)