from utils import bfs, print_flow_matrix

def ford_fulkerson(n, capacities):
    # Initialisation
    residual_graph = [row[:] for row in capacities]
    flow_matrix = [[0] * n for _ in range(n)]
    max_flow = 0
    s, t = 0, n-1  # Source et puits
    iteration = 0
    
    print("=== Initialisation ===")
    
    while True:
        iteration += 1
        parent = [-1] * n
        if not bfs(residual_graph, n, s, t, parent):
            break
            
        # Trouver le chemin et le flot maximal
        path_flow = float("inf")
        path = []
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            path.append((u, v))
            v = u
        path.reverse()  # Pour afficher de la source au puits
        
        print(f"\n=== Itération {iteration} ===")
        print(f"Chemin améliorant: {' -> '.join(f'{u}->{v}' for u,v in path)}")
        print(f"Flot pouvant être ajouté: {path_flow}")
        
        # Mise à jour des flots
        v = t
        while v != s:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            flow_matrix[u][v] += path_flow
            v = u
        
        max_flow += path_flow
        
        print("\nMatrice de flot actuelle:")
        print_flow_matrix(flow_matrix, capacities)
        
    
    print(f"\n=== Résultat final ===")
    print(f"Flot maximal: {max_flow}")
    print("Matrice de flot finale:")
    print_flow_matrix(flow_matrix, capacities)
    
    return max_flow, flow_matrix