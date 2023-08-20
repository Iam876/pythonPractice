import time
from collections import defaultdict

def DfsShortestPath(graph, start, end):
    stack = [(start, [start])]
    visited = []
    iteration = 0

    while stack:
        node, path = stack.pop()

        if node not in visited:
            visited.append(node)
            
            if node == end:
                return path, visited
                
            iteration += 1
            print(f"\n######## Stack processing step {iteration} #############\n")

            print("Stack:", [n for n, _ in stack])
            pushedNodes = []
            time.sleep(1)
            print(f"Visiting node : '{node}'")
            time.sleep(1)
            print("Visited nodes:", visited)
            time.sleep(1)
            for neighbor in graph[node][::-1]:  # Reversed order to match the desired sequence
                if neighbor not in visited and neighbor not in [n for n, _ in stack]:
                    stack.append((neighbor, path + [neighbor]))  # Mark as visited right before pushing
                    pushedNodes.append(neighbor)

            if pushedNodes:
                print(f"Pushing nodes: {', '.join(pushedNodes)}")

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

# Find the shortest path using DFS
ShortestPath, visited_nodes = DfsShortestPath(graph, StartNode, EndNode)

if ShortestPath:
    print("\n########### Stack Process Done ##########\n")
    print(f"Shortest path from {StartNode} to {EndNode}: {' -> '.join(ShortestPath)}")
    print("Visited nodes:", ', '.join(visited_nodes))
    print("last node : {LastNode}")
else:
    print(f"No path found from {StartNode} to {EndNode}")
