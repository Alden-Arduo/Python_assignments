from collections import deque
import copy

def bubbles(physical_contact_info):
    adj_list = adjacency_list(physical_contact_info)
    comps = connected_component(adj_list)
    return comps


def connected_component(adj_list):
    n = len(adj_list)
    state = ['u'] * n
    Q = deque()
    component = []
    for i in range(n):
        if state[i] == 'u':
            prev_state = copy.deepcopy(state)
            state[i] == 'd'
            Q.append(i)
            bfs_loop(adj_list, Q, state)
            component.append(new_component(prev_state, state))
    return component


def new_component(prev_state, state):
    comp = []
    for i in range(len(prev_state)):
        if prev_state[i] != state[i]:
            comp.append(i)
    return comp


def bfs_loop(adj_list, Q, state):
    while len(Q) > 0:
        u = Q.popleft()
        for v in adj_list[u]:
            if state[v] == 'u':
                state[v] = 'd'
                Q.append(v)
            state[u] = 'p'


def adjacency_list(info):
    info = info.splitlines()
    _, k = info[0].split()
    adj_list = [[i] for i in range(int(k))]
    for edge in info[1:]:
        v1, v2 = edge.split()
        adj_list[int(v1)].append(int(v2))
        adj_list[int(v2)].append(int(v1))
    return adj_list


physical_contact_info = """\
U 2
0 1
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 2
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 0
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 1
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 4
2 1
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))


physical_contact_info = """\
U 7
1 4
2 0
4 6
5 3
"""
print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))