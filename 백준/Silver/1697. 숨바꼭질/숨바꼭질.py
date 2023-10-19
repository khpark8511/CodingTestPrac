from collections import deque
global k,n
n,k = map(int,input().split())
graph = [0]* 1000000

def bfs(x):
    global n,k 
    queue = deque()
    queue.append(x)
    graph[x] = 0
    while queue :
        v = queue.popleft()
        #print('v,graph[v]: ',v,graph[v])
        if v == k :
            return graph[v]
        for i in range(3):
            if i == 0 :
                nv = v-1
            elif i == 1 :
                nv = v+1
            else :
                nv = 2*v
            if nv < 0 or nv > 100000:
                continue
            else:
                if not graph[nv]:
                    queue.append(nv)
                    graph[nv] = graph[v]+1 

     
print(bfs(n))
    