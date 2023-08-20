import time
from collections import defaultdict, deque

def BfsShortestPath(graph, start, end):
    queue = deque([(start, [start])])
    visited = []
    iteration = 0

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            visited.append(node)
            
            if node == end:
                return path, visited
            iteration += 1
            print(f"\n######## Queue processing step {iteration} #############\n")
            print("Queue:", [n for n, _ in queue])
            enqueuedNodes = []
            time.sleep(1)
            print(f"Visiting node : '{node}'")
            time.sleep(1)
            print("Visited nodes:", visited)
            time.sleep(1)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    enqueuedNodes.append(neighbor)

            if enqueuedNodes:
                print(f"Enqueuing nodes: {', '.join(enqueuedNodes)}")
                queue.extend((neighbor, path + [neighbor]) for neighbor in enqueuedNodes)

            time.sleep(1)
            
    return None, visited

# Create the graph as an adjacency list
def create_graph():
    graph = defaultdict(list)
    n = int(input("Enter the number of edges: "))
    for _ in range(n):
        u, v = input("Enter edge (u v): ").split()
        graph[u].append(v)
        graph[v].append(u)
    return graph

# Take user inputs for graph, starting node, and destination node
graph = create_graph()
StartNode = input("Enter the starting node: ")
EndNode = input("Enter the destination node: ")
print("\n")

# Find the shortest path using BFS
ShortestPath, visited_nodes = BfsShortestPath(graph, StartNode, EndNode)

if ShortestPath:
    print("\n########### Queue Process Done ##########\n")
    print(f"Shortest path from {StartNode} to {EndNode}: {' -> '.join(ShortestPath)}")
    print("Visited nodes:", ', '.join(visited_nodes))
else:
    print(f"No path found from {StartNode} to {EndNode}")


