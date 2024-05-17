graph_acyc = {
    0: [1, 2],
    1: [0],
    2: [0]
}

graph_cyc = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}


def dfs(graph, start, prev):
    global visited, cyc
    visited[start] = True
    for vertex in graph[start]:
        if visited[vertex] and vertex != prev:
            cyc = True
        elif not visited[vertex]:
            dfs(graph, vertex, start)

visited = [False] * len(graph_cyc)
cyc = False
dfs(graph_cyc, 0, 0)
print(cyc)
