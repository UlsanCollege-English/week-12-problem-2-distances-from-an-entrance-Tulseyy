
from collections import deque


def bfs_distances(graph, start):
    """
    Compute shortest distances (in edges) from start to all reachable nodes
    in an unweighted graph.

    graph: dict mapping stage name (string) to list of neighbor stage names.
    start: starting stage name (string).

    Return value:
        - A dict dist where dist[node] is the minimum number of edges
          from start to node.
        - dist[start] should be 0.
        - Only include reachable nodes.
        - If start is not in graph, return {}.
    """
    # If start node is not in the graph, return empty dict
    if start not in graph:
        return {}
    
    # Initialize distance dict and queue for BFS
    dist = {start: 0}
    queue = deque([start])
    
    # Process nodes level by level
    while queue:
        current = queue.popleft()
        current_dist = dist[current]
        
        # Explore all neighbors of current node
        for neighbor in graph[current]:
            # If neighbor not yet visited, record distance and add to queue
            if neighbor not in dist:
                dist[neighbor] = current_dist + 1
                queue.append(neighbor)
    
    return dist


if __name__ == "__main__":
    # Optional simple check
    sample_graph = {
        "Gate": ["Stage1", "Stage2"],
        "Stage1": ["Gate", "Stage3"],
        "Stage2": ["Gate"],
        "Stage3": ["Stage1"],
    }
    d = bfs_distances(sample_graph, "Gate")
    print("Distances from Gate:", d)
