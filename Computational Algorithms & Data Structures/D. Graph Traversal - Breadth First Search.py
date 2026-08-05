# Imports the double-ended-queue (deque) class from Python3's
# Collections module.
from collections import deque

# This Graph Traversal example uses the Breadth-First Search
# technique to iterate across a graph, to a time complexity
# of O(V+E): Linear Graph Time.
def bfs(start):

    # Initialises both a deque variable, so as to be accessed
    # from either end; and a set. In this example, the
    # 'start' variable populates the staring node with 'A'.
    queue = deque([start])
    visited = set([start])

    # Matches a non-empty (truthy) 'queue' variable, to
    # initialise a while-loop.
    while queue:

        # Defines the 'node' variable as the left-most value
        # in the 'queue' deque, and then prints. To do this,
        # 'popleft' removes and returns the last-in value (LIFO).
        node = queue.popleft()

        print(node)

        # Iterates through each adjacency list-item for a
        # given node on the 'graph' dictionary, starting with
        # 'A', as specified in this example.
        for neighbour in graph[node]:

            # For each element mapped to the dictionary's index,
            # e.g. 'B' in 'A', the element is added/appended to
            # the 'visited' and 'queue' variables, so that each
            # element is printed before the next index is visited.
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Initialises our input graph for the 'bfs' function.
graph = {
    "A":["B","C"],
    "B":["D"],
    "C":[],
    "D":[]
}


# Calls the function, specifying a beginning node.
bfs("A")
