from collections import deque


def bfs_shortest_path(graph, start, target):
    if start == target:
        return [start]

    # Initialize the queue with the start node and a path list
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current_node, path = queue.popleft()
        print("current node", current_node)
        print("path", path)
        print("current queue", queue)

        # Check all the neighbors of the current node
        for neighbor in graph[current_node]:
            print("---")
            print(neighbor)
            print(graph[current_node])
            print("---")
            if neighbor == target:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                print(queue)
                print("XXXXXX")

    # If the loop ends without finding the target
    return None


# Example usage
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

start = "A"
target = "K"
path = bfs_shortest_path(graph, start, target)

if path:
    print("Shortest path:", " -> ".join(path))
else:
    print("No path exists between", start, "and", target)
