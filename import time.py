import time
from collections import defaultdict, deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = []

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            visited.append(node)

            if node == end:
                return path, visited
            print("Queue:", [n for n, _ in queue])
            enqueued_nodes = []
            time.sleep(1)
            print(f"Visiting node : '{node}'")
            time.sleep(1)
            print("Visited nodes:", visited)
            time.sleep(1)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    enqueued_nodes.append(neighbor)

            if enqueued_nodes:
                print(f"Enqueuing nodes: {', '.join(enqueued_nodes)}")
                queue.extend((neighbor, path + [neighbor]) for neighbor in enqueued_nodes)

            time.sleep(1)
            print(f"######## Queue running {queue} #############")
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
start_node = input("Enter the starting node: ")
end_node = input("Enter the destination node: ")

# Find the shortest path using BFS
shortest_path, visited_nodes = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")
    print("Visited nodes:", ', '.join(visited_nodes))
else:
    print(f"No path found from {start_node} to {end_node}")
