from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend([n for n in graph[vertex] if n not in visited])
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
start_node = 2
bfs_result = bfs(graph, start_node)
dfs_result = dfs(graph, start_node)
print("BFS:", bfs_result)
print("DFS:", dfs_result)
