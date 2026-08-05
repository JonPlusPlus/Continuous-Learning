# This Graph Traversal example uses the Depth-First Search
# technique to demonstrate interation down a graph, to a
# time complexity of O(V+E): Linear Graph Time.
def dfs(node, visited):

    # If a node is already in the 'visited' set, the function
    # returns, preventing cycling through the same node.
    if node in visited:
        return

    # Following a FALSE match to the above if-statement,
    # the function adds the newly read node to the set.
    visited.add(node)

    # The newly read node is printed. In the example, upon
    # first pass, this will be 'A'.
    print(node)

    # For example, we iterate over neighbour 'B' in graph-node
    # 'A', and initialise a nested function-call to recheck for
    # node in visited, then to add and print said node. This
    # process will then nest down again for neighbour 'D' in
    # graph-node 'B'. Once nodes are looked for in graph-node
    # 'D', the nested-loop exits, as does the nested-loop for
    # graph-node 'B'. We return to graph-node 'A', and repeat
    # for the next neighbor, 'C'.
    for neighbour in graph[node]:
        dfs(neighbour, visited)


# Initialises our input graph for the 'dfs' function.
graph = {
    "A":["B","C"],
    "B":["D"],
    "C":[],
    "D":[]
}


# Calls the function, specifying a beginning node.
dfs("A", set())
