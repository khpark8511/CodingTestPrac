n = int(input())
graph = []
cnt = 0 
global hcnt 
hcnt = 0 
hcntlist = [] 
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    global hcnt 
    if 0<=x<n and 0<=y<n and graph[x][y] == 1 :
        graph[x][y] = 0 
        hcnt += 1 
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return 1 
    return False

for i in range(n):
    for j in range(n):
        res = dfs(i,j)
        if  res == 1 :
            cnt += res
            hcntlist.append(hcnt)
            hcnt = 0 
print(cnt)
hcntlist.sort()
for i in range(len(hcntlist)):
    print(hcntlist[i])
            

