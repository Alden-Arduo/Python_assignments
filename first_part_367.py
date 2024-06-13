from search import *
import math
from heapq import *

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
            self.graph.append(item)  # prints all the stuff in the map_str in list form for every row separately.
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
            print(movement)
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
    


map_str = """\
+-------+
|  9  XG|
|X XXX P|
| S  0FG|
|XX P XX|
+-------+
"""

graph = RoutingGraph(map_str)

print("Starting nodes:", sorted(graph.starting_nodes()))
print("Outgoing arcs (available actions) at starting states:")
for s in sorted(graph.starting_nodes()):
    print(s)
    for arc in graph.outgoing_arcs(s):
        print ("  " + str(arc))

node = (1,1,5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (1,7,2)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (3, 7, 0)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3, 7, math.inf)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3, 6, 5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (3, 6, 9)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (2, 7, 4)  # at a location with a portal
print("\nOutgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

print("_")    
    
    
map_str = """\
+--+
|GS|
+--+
"""

graph = RoutingGraph(map_str)

print("Starting nodes:", sorted(graph.starting_nodes()))
print("Outgoing arcs (available actions) at the start:")
for start in graph.starting_nodes():
    for arc in graph.outgoing_arcs(start):
        print ("  " + str(arc))



node = (1,1,1)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))
    

print("_")

map_str = """\
+------------+
|    P       |
| 7          |
|XXXX        |
|P F X  G    |
+------------+
"""

print("_")

map_str = """\
+------+
|S    S|
|  GXXX|
|S     |
+------+
"""

graph = RoutingGraph(map_str)
print("Starting nodes:", sorted(graph.starting_nodes()))