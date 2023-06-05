n,k = map(int,input().split())
graph = list(map(int,input().split()))

graph.sort(reverse=True)
print(graph[k-1])


