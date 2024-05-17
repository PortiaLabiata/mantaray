from math import inf

graph = [
    [0, 1, 3, 0],
    [1, 0, 1, 4],
    [3, 1, 0, 2],
    [0, 4, 2, 0]
]
n = len(graph)
dist = [[0]*n for _ in range(n)]

for i in range(0, n):
    for j in range(0, n):
        if i == j: continue
        elif graph[i][j]: dist[i][j] = graph[i][j]
        else: dist[i][j] = inf

for i in range(0, n):
    for j in range(0, n):
        for k in range(0, n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

print(dist[0], sep='\n')
