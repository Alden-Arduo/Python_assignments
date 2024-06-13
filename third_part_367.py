from search import *
from heapq import *
import math

class RoutingGraph(Graph):

    def __init__(self, map_str):
        """
        Initialises the routing graph.
        """

        self.map_str = map_str
        self.starting_list = []
        self.goal_nodes = []
        self.graph_chars = ['+', '|', '-', 'X']
        self.graph = []
        for item in self.map_str.strip().split("\n"):
            self.graph.append(item) # prints all the stuff in the map_str in list form for every rows separately.
        #print(self.graph)
      
        for row_index in range(len(self.graph)):
            for col_index in range(len(self.graph[row_index])):
                i,j = row_index, col_index

                if self.graph[i][j] == 'S': 
                    self.starting_list.append((i, j, math.inf))
                elif self.graph[i][j].isdigit(): 
                    self.starting_list.append((i, j, int(self.graph[i][j])))
                elif self.graph[i][j] == 'G': 
                    self.goal_nodes.append((i, j))
    
    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed. """
        
        s_nodes = []
        for node in self.starting_list:
            s_nodes.append(node)
        return s_nodes
    

    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""
       

        directions = [('N' , -1, 0),
                 ('E' ,  0, 1),
                 ('S' ,  1, 0),
                 ('W' ,  0, -1),] 


        for movement in directions:
            #print(movement)
            i =  tail_node[0] + movement[1]
            j =  tail_node[1] + movement[2]
            fuel = tail_node[2]
            
            if self.graph[i][j] not in self.graph_chars and fuel > 0:
                head_node = (i, j, fuel - 1)
                yield Arc(tail_node, head_node, movement[0], 5)

        if self.graph[tail_node[0]][tail_node[1]] == 'F' and fuel < 9:
            head_node = (tail_node[0], tail_node[1], 9)
            yield Arc(tail_node, head_node, "Fuel up", 15)
        
        if self.graph[tail_node[0]][tail_node[1]] == 'P':
            for row_index in range(len(self.graph)):
                for col_index in range(len(self.graph[row_index])):
                    i,j = row_index, col_index
    
                    if self.graph[i][j] == 'P' and (i,j) != (tail_node[0],tail_node[1]): 
                        head_node = (i, j, fuel)
                        yield Arc(tail_node, head_node, "Teleport to ({}, {})".format(i,j), 10)                 


    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""
        
        est_cost = []
        for goal in self.goal_nodes:
            dist = (abs(goal[0] - node[0]) + abs(goal[1] - node[1]))
            min_dist = dist * 5
            est_cost.append(min_dist)
        return min(est_cost)

    def is_goal(self, node):
        return (node[0], node[1]) in self.goal_nodes


class AStarFrontier(Frontier):
    """ AStar searching alogirthm with heuristics approach """

    def __init__(self, graph):
        """ Initialises the AStarFrontier """
        self.map_graph = graph
        self.visited = set()
        self.prio_queue = []
        self.counter = 1

    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.
        """
        if path[-1].head not in self.visited:
            move_cost = 0
            for move in path:
                move_cost += move.cost

            heappush(self.prio_queue, (self.map_graph.estimated_cost_to_goal(path[-1].head) + move_cost, self.counter, path)) # creates a tuple inside with the total move_cost, counter and its path.
            self.counter += 1
    
    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception.
        """
        while self.prio_queue:
            path = heappop(self.prio_queue)[2] # gets the path or the one with arc.
            #print(path[-1].head) #this gives the head of the arc

            if path[-1].head not in self.visited:
                self.visited.add(path[-1].head)
                return path
        raise StopIteration

def print_map(map_graph, frontier, solution):

    map_char = [list(item) for item in map_graph.graph] # converts each element
    #in a row into its own index for string assignment below
    
    if solution:
        for arc in solution:
            i, j = arc.head[0], arc.head[1]
            if map_char[i][j] == " ":
                map_char[i][j] = '*'    
    
    for path in frontier.visited:
        i, j = path[0], path[1]
        if map_char[i][j] == " ":
            map_char[i][j] = '.'    
    
    for map_ele in map_char:
        #print(map_ele)
        map_env = ''.join(map_ele)
        print(map_env)     
    

#---


print("_")
map_str = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)

print("_")
map_str = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""


map_graph = RoutingGraph(map_str)
# changing the heuristic so the search behaves like LCFS
map_graph.estimated_cost_to_goal = lambda node: 0

frontier = AStarFrontier(map_graph)

solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)

print("_")
map_str = """\
+-------------+
| G         G |
|      S      |
| G         G |
+-------------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)

print("_")
map_str = """\
+-------+
|     XG|
|X XXX  |
|  S    |
+-------+
"""
map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)

print("_")
map_str = """\
+--+
|GS|
+--+
"""
map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)

print("_")
map_str = """\
+----+
|    |
| SX |
| X G|
+----+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)

print("_")
map_str = """\
+---------------+
|    G          |
|XXXXXXXXXXXX   |
|           X   |
|  XXXXXX   X   |
|  X S  X   X   |
|  X        X   |
|  XXXXXXXXXX   |
|               |
+---------------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)

print("_")
map_str = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)