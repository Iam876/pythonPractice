import time
from collections import defaultdict, deque

# BFS
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

# DFS
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

def shortest(StartNode, EndNode, ShortestPath, visited_nodes):
    if ShortestPath:
        print("\n########### Process Done ##########\n")
        print(f"Shortest path from {StartNode} to {EndNode}: {' -> '.join(ShortestPath)}")
        print("Visited nodes:", ', '.join(visited_nodes))
    else:
        print(f"No path found from {StartNode} to {EndNode}")

def main():
    print("Which operation do you want to perform?")
    print("BFS -> Choose 1 || DFS -> Choose 2")
    
    check = int(input("Please Enter your choice: "))
    
    if check == 1:
        print("########## BFS STARTING ##########")
    elif check == 2:
        print("########## DFS STARTING ##########")
    else:
        print("Wrong input !! Please choose (1 or 2)")
    graph = create_graph()
    StartNode = input("Enter the starting node: ")
    EndNode = input("Enter the destination node: ")
    print("\n")
    
    if check == 1:
        ShortestPath, visited_nodes = BfsShortestPath(graph, StartNode, EndNode)
        shortest(StartNode, EndNode, ShortestPath, visited_nodes)
    elif check == 2:
        ShortestPath, visited_nodes = DfsShortestPath(graph, StartNode, EndNode)
        shortest(StartNode, EndNode, ShortestPath, visited_nodes)
    else:
        print("Wrong input!!! please input (1 or 2)")

if __name__ == "__main__":
    main()