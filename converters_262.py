def format_sequence(converters_info, source_format, destination_format):
    adj_list = adjacency_list(converters_info)
    result = []
    dfs_backtrack([source_format], adj_list, destination_format, result)
    return shortest_converter(result)
    
    
def shortest_converter(result):
    min_len = float('inf')
    final_result = []
    if result != []:  
        for i in result:
            if len(i) < min_len:
                min_len = len(i)
                final_result = i
    else:
        return 'No solution!'
    return final_result


def dfs_backtrack(candidate, adj_list, destination, result):
    if is_solution(candidate, destination):
        add_to_output(candidate, result)
    else:
        for child in children(candidate, adj_list):
            dfs_backtrack(child, adj_list, destination, result)


def add_to_output(candidate, result):
    result.append(candidate)


def is_solution(candidate, destination):
    return candidate[-1] == destination


def children(candidate, adj_list):
    res = []
    for i in adj_list[candidate[-1]]:
        temp = list(candidate)
        if i not in temp:
            temp.append(i)
            res.append(temp)
    return res


def adjacency_list(converters_info):
    converters_info = converters_info.splitlines()
    _, k = converters_info[0].split()
    adj_list = [[] for _ in range(int(k))]
    for pair in converters_info[1:]:
        v1, v2 = pair.split()
        adj_list[int(v1)].append(int(v2))
    return adj_list


converters_info_str = """\
D 2
0 1
"""

source_format = 0
destination_format = 1

print(format_sequence(converters_info_str, source_format, destination_format))

converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 1))

converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 0))

converters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""

print(format_sequence(converters_info_str, 1, 2))

converters_info_str = """\
D 1
"""

print(format_sequence(converters_info_str, 0, 0))