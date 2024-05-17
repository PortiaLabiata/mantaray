import heapq

edges = [
    (0, 1, 3),
    (0, 5, 5),
    (5, 1, 6),
    (1, 2, 5),
    (2, 3, 9),
    (2, 4, 3),
    (3, 4, 7),
    (4, 5, 2)
]
n = 6

graph = {i: [] for i in range(0, n)}

for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))

def prim(graph):
    tree = []
    visited = set()
    start_vertex = list(graph.keys())[0]
    edges = [(weight, start_vertex, adjacent) for adjacent, weight in graph[start_vertex]]
    heapq.heapify(edges)

    while edges:
        print(edges)
        weight, start, end = heapq.heappop(edges)
        if end not in visited:
            tree.append((start, end, weight))
            visited.add(end)

            for adjacent, weight in graph[end]:
                if adjacent not in visited:
                    heapq.heappush(edges, (weight, end, adjacent))
    return tree

tree = prim(graph)
weight = sum([w for _, _, w in tree])
print(tree)
print(weight)
