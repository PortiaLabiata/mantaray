from collections import deque

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}

def bfs(graph, start, visited, component):
    visited[start] = True
    d = deque()
    d.append(start)
    component.append(start)
    while len(d) > 0:
        vertex = d.popleft()
        for adjacent in graph[vertex]:
            if not visited[adjacent]:
                d.append(adjacent)
                visited[adjacent] = True
                component.append(adjacent)


visited = [False] * len(graph)
components = []
for vertex in graph:
    if visited[vertex]: continue
    component = []
    bfs(graph, vertex, visited, component)
    components.append(component)
print(components)
