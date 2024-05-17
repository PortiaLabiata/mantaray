from sys import exit

graph_bichrom = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

graph_not_bichrom = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0, 3],
    3: [0, 1, 2]
}

def dfs(graph, start, color=True):
    global colors
    colors[start] = color
    for vertex in graph[start]:
        print(colors, vertex)
        if colors[vertex] is None:
            dfs(graph, vertex, not color)
        else:
            if colors[vertex] == color:
                print('Not bichromatic')
                exit()
    print('Bichromatic')

colors = [None] * len(graph_bichrom)
dfs(graph_bichrom, 0)
