n = int(input())
graph = [[] for x in range(n+1)]

for i in range(n):
    graph[i] = list(map(int,input()))

def dfs(x,y):
    global cnt 
    if x < 0 or y <0 or x >= n or y >= n :
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1 
         
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)  
        return True
    return False
global cnt
cnt = 0 
res = 0
resList = [] 
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:      
            resList.append(cnt)
            res += 1
            cnt = 0    
print(res)
resList.sort()
for i in resList:
    print(i)
