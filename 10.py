graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4, 5],
    4: [3],
    5: [3]
}

def dfs(graph, start):
    global visited
    visited[start] = True
    for vertex in graph[start]:
        if not visited[vertex]:
            dfs(graph, vertex)

visited = [False] * len(graph)
components = 0
for vertex in graph.keys():
    if not visited[vertex]:
        dfs(graph, vertex)
        components += 1
print(components)

