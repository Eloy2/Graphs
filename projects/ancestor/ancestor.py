
# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    # Make empty graph
    graph = {}
    ################ Fill in graph
    for family in ancestors:
        if family[0] in graph:
            graph[family[0]].add(family[1])
        else:
            graph[family[0]] = {family[1]}
    ############## {1: {3}, 2: {3}, 3: {6}, 5: {6, 7}, 4: {8, 5}, 8: {9}, 11: {8}, 10: {1}}
    # Make stack and add staring node to it.
    stack = []
    stack.append(starting_node)
    times_lopped = 0

    while len(stack) > 0:
        current_node = stack.pop()
        for k,v in graph.items():
            if current_node in v: # if it has parent
                stack.append(k) # add parent to stack
                times_lopped += 1

    if times_lopped == 0: # no parent was found therefore return -1 as per README
        return -1
    else:
        return current_node

# print(earliest_ancestor(test_ancestors, 11))