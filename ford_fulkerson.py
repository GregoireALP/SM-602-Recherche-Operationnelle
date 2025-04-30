from collections import deque

def bfs(residual_graph, n, s, t, parent):
    visited = [False] * n
    queue = deque()
    queue.append(s)
    visited[s] = True
    
    while queue:
        u = queue.popleft()
        
        for v in range(n):
            if not visited[v] and residual_graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
    return False

def ford_fulkerson(n, capacities):
    # Initialisation
    residual_graph = [row[:] for row in capacities]
    flow_matrix = [[0] * n for _ in range(n)]
    max_flow = 0
    s, t = 0, n-1  # Source et puits
    
    parent = [-1] * n
    
    # Algorithme principal
    while bfs(residual_graph, n, s, t, parent):
        # Trouver la capacité résiduelle minimale
        path_flow = float("inf")
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u
        
        # Mettre à jour les flots et capacités résiduelles
        v = t
        while v != s:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            flow_matrix[u][v] += path_flow
            v = u
        
        max_flow += path_flow
    
    return max_flow, flow_matrix