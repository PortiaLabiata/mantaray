from operator import itemgetter

graph = [
    (0, 1, 3),
    (0, 5, 5),
    (5, 1, 6),
    (1, 2, 5),
    (2, 3, 9),
    (2, 4, 3),
    (3, 4, 7),
    (4, 5, 2)
]

graph.sort(key=itemgetter(2))

def kruskal(graph):
    tree = []
    forest = {}

    def make_set(vertex):
        forest[vertex] = vertex

    def find_set(vertex):
        if vertex != forest[vertex]:
            forest[vertex] = find_set(forest[vertex])
        return forest[vertex]

    def unite(a, b):
        root_a = find_set(a)
        root_b = find_set(b)
        forest[root_a] = root_b

    for a, b, w in graph:
        if a not in forest:
            make_set(a)
        if b not in forest:
            make_set(b)

    for a, b, w in graph:
        print(forest)
        if find_set(a) != find_set(b):
            tree.append((a, b, w))
            unite(a, b)

    return tree

tree = kruskal(graph)
weight = sum([w for _, _, w in tree])
print(tree)
print(weight)
