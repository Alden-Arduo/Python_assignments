import math

def min_capacity(city_map, depot_position):
    city_map = city_map.replace("\n", " ")
    map_data = city_map.split(" ")

    # delete unnecessary data
    map_data.pop()
    map_data.pop(0)
    map_data.pop(0)

    # number of vertices in the graph
    V = int(map_data[1])

    graph = []
    # creating the graph with all the edges
    for i in range(3, len(map_data), 3):
        u, v, w = int(map_data[i]), int(map_data[i + 1]), int(map_data[i + 2])
        graph.append((u, v, w))
        graph.append((v, u, w))
        
    # this is the adjacency list graph

    # shortest path distance from depot_position to all other cities
    dist = get_shortest_path(graph, V, depot_position)
    max_dist = 0
    for d in dist:
        if d != float('inf') and d > max_dist:
            max_dist = d

    # calculate min_battery_capacity based on the requirements
    min_battery_capacity = int(math.ceil(max_dist * 12 * 3 * 1.25))
    return min_battery_capacity


# returns shortest path distance from depot_position to all other cities
# using bellman-ford algorithm
def get_shortest_path(graph, V, src):
    # Initialize distances from src to all other vertices
    # as INFINITE
    dist = [float("inf")] * V
    dist[src] = 0

    # Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    for i in range(V - 1):
        # Update dist value and parent index of the adjacent vertices of
        # the picked vertex. Consider only those vertices which are still in
        # queue
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # check for negative-weight cycles. The above step
    # guarantees shortest distances if graph doesn't contain
    # negative weight cycle. If we get a shorter path, then there
    # is a cycle.

    for u, v, w in graph:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    return dist
        
    
# testing the code

city_map1 = """ 
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map1, 0))
print(min_capacity(city_map1, 1))
print(min_capacity(city_map1, 2))
    
    