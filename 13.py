graph = {
    0: [2],
    1: [0],
    2: [1, 4, 5],
    3: [2],
    4: [3],
    5: [6],
    6: [7],
    7: [5]
}

def inverse(graph):
    inversed = {i: [] for i in graph.keys()}
    for vertex in graph:
        for adjacent in graph[vertex]:
            inversed[adjacent].append(vertex)
    return inversed

def dfs(graph, start, visited, stack):
    visited[start] = True
    for vertex in graph[start]:
        if not visited[vertex]:
            visited[vertex] = True
            print(f'Entering vertex {vertex}')
            dfs(graph, vertex, visited, stack)
    stack.append(vertex)

def kosaraju(graph):
    visited = [False] * len(graph)
    stack = []
    for vertex in graph:
        if not visited[vertex]:
            dfs(graph, vertex, visited, stack)

    print(stack)
    inversed = inverse(graph)
    visited = [False] * len(inversed)
    components = []
    while len(stack) > 0:
        vertex = stack.pop()
        if not visited[vertex]:
            component = []
            dfs(inversed, vertex, visited, component)
            components.append(component)

    return components

print(kosaraju(graph))

