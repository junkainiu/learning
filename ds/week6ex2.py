import sys


def is_escapable(vertex, first=False):
    if first:
        x_dis = 50 - abs(vertex[0]) - 7.5
        y_dis = 50 - abs(vertex[1]) - 7.5
    else:
        x_dis = 50 - abs(vertex[0])
        y_dis = 50 - abs(vertex[1])

    if x_dis <= distance:
        return True
    elif y_dis <= distance:
        return True
    else:
        return False


def make_graph(input_list):
    graph = {item: [False] for item in input_list}
    for i, pos in enumerate(input_list):
        if i < len(input_list) - 1:
            for target in input_list[i+1:]:
                if calc_distance(pos, target, i) <= distance:
                    graph[pos].append(target)
                    graph[target].append(pos)
    return graph


def calc_distance(source, target, i):
    x_dis = abs(source[0] - target[0])
    y_dis = abs(source[1] - target[1])
    if i == 0:
        return (x_dis ** 2 + y_dis ** 2) ** 0.5 - 7.5
    else:
        return (x_dis ** 2 + y_dis ** 2) ** 0.5


def dfs_search(graph, pos):
    if pos[2] is True:
        print 'Yes'
        sys.exit()
    else:
        if graph[pos][0] is False:
            graph[pos][0] = True
            for vertex in graph[pos][1:]:
                pos = vertex
                dfs_search(graph, pos)


c_count, distance = map(int, raw_input().split(' '))
if is_escapable((0, 0), first=True):
    print 'Yes'
else:
    input_list = [(0, 0, False)]
    init = (0, 0, False)
    for item in range(c_count):
        vertex = map(int, raw_input().split(' '))
        if is_escapable(vertex):
            vertex.append(True)
        else:
            vertex.append(False)
        input_list.append(tuple(vertex))
    graph = make_graph(input_list)
    dfs_search(graph, init)
    print 'No'
