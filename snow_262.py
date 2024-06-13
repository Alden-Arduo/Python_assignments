def which_segments(city_map):
    adj_list = adjacency_list(city_map)
    res = []
    parent = prim(adj_list, 0)
    segment(parent, res)
    return res


def adjacency_list(info):
    info = info.splitlines()
    _, k, W = info[0].split()
    adj_list = [[] for _ in range(int(k))]
    for edge in info[1:]:
        v1, v2, w = edge.split()
        adj_list[int(v1)].append([int(v2), int(w)])
        adj_list[int(v2)].append([int(v1), int(w)])
    return adj_list


def prim(adj_list, s):
    n = len(adj_list)
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n
    distance[s] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, w in adj_list[u]:
            if not in_tree[v] and w < distance[v]:
                distance[v] = w
                parent[v] = u
    return parent


def next_vertex(in_tree, distance):
    min_dist = float('inf')
    next_vertex = 0
    for i in range(len(in_tree)):
        if not in_tree[i] and distance[i] <= min_dist:
            min_dist = distance[i]
            next_vertex = i
    return next_vertex


def segment(parent, res):
    for i in range(1, len(parent)):
        if parent[i] is None:
            res.append((0, i))
        else:
            if i < parent[i]:
                res.append((i, parent[i]))
            else:
                res.append((parent[i], i))



city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""
print(sorted(which_segments(city_map)))

city_map = """\
U 1 W
"""

print(sorted(which_segments(city_map)))