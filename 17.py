from math import inf
import heapq

graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 1), (3, 4)],
    2: [(0, 3), (1, 1), (3, 2)],
    3: [(1, 4), (2, 2)]
}

def dijkstra(graph, start, distances, processed):
    distances[start] = 0
    unvisited = [(0, start)]
    while len(unvisited) > 0:
        distance, vertex = heapq.heappop(unvisited)
        if processed[vertex]: continue
        processed[vertex] = True

        for adjacent, weight in graph[vertex]:
            updated = distances[vertex] + weight
            if updated < distances[adjacent]:
                distances[adjacent] = updated
                heapq.heappush(unvisited, (updated, adjacent))

distances = [inf for _ in graph]
processed = [False for _ in graph]
dijkstra(graph, 0, distances, processed)
print(distances)
