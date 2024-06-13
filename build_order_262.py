def build_order(dependencies):
    adj_list = adjacency_list(dependencies)
    state = ['u'] * len(adj_list)
    parent = [None] * len(adj_list)
    stack = []
    for i in range(len(adj_list)):
        if state[i] == 'u':
            dfs_loop(adj_list, i, state, stack)
    return stack[::-1]


def dfs_loop(adj_list, u, state, stack):
    for v in adj_list[u]:
        if state[v[0]] == 'u':
            state[v[0]] = 'd'
            dfs_loop(adj_list, v[0], state, stack)
    state[u] = 'p'
    stack.append(u)
    
    
def adjacency_list(dependencies):
    dependencies = dependencies.splitlines()
    _, k = dependencies[0].split()
    adj_list = [[] for _ in range(int(k))]
    for edge in dependencies[1:]:
        v1, v2 = edge.split()
        adj_list[int(v1)].append([int(v2)])
    return adj_list


dependencies = """\
D 2
0 1
"""
print(build_order(dependencies))

dependencies = """\
D 3
1 2
0 2
"""
print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])

dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))