n = int(input())
graph = []
for i in range(n):
    graph.append(int(input()))

graph.sort()
for i in range(len(graph)):
    print(graph[i])


