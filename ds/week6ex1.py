vertex_count, edge_count = map(int, raw_input().split(' '))
from collections import deque


def init_graph(vertex_count):
    return [[False] for _ in range(vertex_count)]

graph = init_graph(vertex_count)

for i in range(edge_count):
    start_vertex, end_vertex = map(int, raw_input().split(' '))
    graph[start_vertex].append(end_vertex)
    graph[end_vertex].append(start_vertex)

graph = [sorted(vertex) for vertex in graph]


def print_res(res):
    for group in res:
        output = ['{']
        for i in group:
            output.append(str(i))
        output.append('}')
        print ' '.join(output)


def list_components(graph, method):
    all_res = []
    for i, vertex in enumerate(graph):
        if vertex[0] is False:
            if method == 'dfs':
                res = [i]
                dfs_search(graph, vertex, res)
            else:
                res = [i]
                bfs_search(graph, vertex, res)
            all_res.append(res)
    print_res(all_res)


def dfs_search(graph, vertex, res):
    if vertex[0] is False:
        vertex[0] = True
        for i in vertex[1:]:
            if graph[i][0] is False:
                res.append(i)
            dfs_search(graph, graph[i], res)


def bfs_search(graph, vertex, res):
    stack = deque([res.pop()])
    while stack:
        v = stack.popleft()
        if graph[v][0] is False:
            res.append(v)
            graph[v][0] = True
            for i in graph[v][1:]:
                stack.append(i)

from copy import deepcopy
list_components(deepcopy(graph), 'dfs')
list_components(deepcopy(graph), 'bfs')
