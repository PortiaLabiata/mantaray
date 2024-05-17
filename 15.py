from math import inf
from collections import deque

graph - {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 4],
    3: [0, 4],
    4: [2, 3]
}

def bfs(graph, start, visited):
    visited[start] = True
    distances[start] = 0
    queue = deque()
    queue.append(start)
    prev_vertex = start
    len_cycle = inf
    while len(queue) > 0:
        vertex = queue.popleft()
        for adjacent in graph[vertex]:
            if adjacent == start and adjacent != prev_vertex:
                len_cycle = min(len_cycle, distances[prev_vertex] + 1)

visited = [False] * len(graph)
bfs(graph, 0, visited)
