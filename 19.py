from math import inf

n = 5
graph = [
    (0, 1, 2),
    (0, 3, 7),
    (0, 2, 3),
    (1, 3, 3),
    (1, 4, 5),
    (4, 3, 2),
    (3, 2, -2)
]
m = len(graph)

distances = [inf] * n
distances[0] = 0
for _ in range(0, n-1):
    for a, b, w in graph:
        distances[b] = min(distances[b], distances[a] + w)

print(distances)
