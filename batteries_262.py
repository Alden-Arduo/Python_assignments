def adjacency_list(info):
    info = info.splitlines()
    _, k, W = info[0].split()
    adj_list = [[] for _ in range(int(k))]
    for edge in info[1:]:
        v1, v2, w = edge.split()
        adj_list[int(v1)].append([int(v2), int(w)])
        adj_list[int(v2)].append([int(v1), int(w)])
    return adj_list


def next_vertex(in_tree, distance):
    min_dist = float('inf')
    next_vertex = 0
    for i in range(len(in_tree)):
        if not in_tree[i] and distance[i] <= min_dist:
            min_dist = distance[i]
            next_vertex = i
    return next_vertex   
    
    
def dijkstra(adj_list, s):
    n = len(adj_list)
    in_tree = [False] * n
    distance = [float('inf')] * n
    distance[s] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True 
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
    return distance
                    
    
def minimum_distance(distance):
    min_distance = 0
    for i in distance:
        if i > min_distance and i != float('inf'):
            min_distance = i
    return min_distance


def min_capacity(city_map, depot_position):
    adj_list = adjacency_list(city_map)
    min_dist = dijkstra(adj_list, depot_position)
    min_distance = minimum_distance(min_dist)
    min_battery_capacity = int(min_distance * 12 * 3 * 1.25)
    return min_battery_capacity 


city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))
print(min_capacity(city_map, 3))