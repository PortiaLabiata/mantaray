from math import inf

graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 1), (3, 4)],
    2: [(0, 3), (1, 1), (3, 2)],
    3: [(1, 4), (2, 2)]
}

def dijkstra(graph, start, distances):
    distances[start] = 0
    unvisited = set(graph.keys())
    while len(unvisited) > 0:
        vertex = min(unvisited, key=distances.__getitem__)
        unvisited.remove(vertex)

        for adjacent, weight in graph[vertex]:
            if adjacent in unvisited:
                distances[adjacent] = min(distances[adjacent], distances[vertex]+weight)

distances = [inf for _ in graph]
dijkstra(graph, 0, distances)
print(distances)
