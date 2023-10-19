from collections import deque
nx = [-2,-2,2,2,1,1,-1,-1]
ny = [1,-1,1,-1,2,-2,2,-2]

def bfs(x,y,ex,ey):
    queue = deque()
    queue.append((x,y))
    while queue:
        a,b = queue.popleft()
        if a == ex and b == ey :
            return graph[a][b]
        else:
            for i in range(8):
                na = a + nx[i]
                nb = b + ny[i]
                if 0 <= na < l and 0 <= nb < l and not graph[na][nb]:
                    queue.append((na,nb))
                    graph[na][nb] = graph[a][b] + 1 
                    
tc = int(input())

for i in range(tc):
    l = int(input())
    graph = [[0]*l for x in range(l)]
    x,y = map(int,input().split())
    ex,ey = map(int,input().split())
    if (x,y) == (ex,ey):
        print(0)
        continue
    else:
        print(bfs(x,y,ex,ey))

