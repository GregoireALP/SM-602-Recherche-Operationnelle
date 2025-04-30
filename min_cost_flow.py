def bellman_ford(n, costs, s):
    distance = [float('inf')] * n
    distance[s] = 0
    
    for _ in range(n-1):
        for u in range(n):
            for v in range(n):
                if distance[u] + costs[u][v] < distance[v]:
                    distance[v] = distance[u] + costs[u][v]
    
    return distance

def min_cost_flow(n, capacities, costs, target_flow):
    # Initialisation
    flow = [[0] * n for _ in range(n)]
    total_flow = 0
    total_cost = 0
    
    while total_flow < target_flow:
        # Étape 1: Trouver le chemin de coût minimal avec Bellman-Ford
        distance = bellman_ford(n, costs, 0)
        
        # Étape 2: Trouver le chemin améliorant
        path = []
        u = n-1
        while u != 0:
            for v in range(n):
                if capacities[v][u] - flow[v][u] > 0 and distance[u] == distance[v] + costs[v][u]:
                    path.append((v, u))
                    u = v
                    break
        
        if not path:
            break  # Plus de chemin améliorant
        
        # Étape 3: Calculer le flot maximal sur ce chemin
        path_flow = min(capacities[v][u] - flow[v][u] for v, u in path)
        path_flow = min(path_flow, target_flow - total_flow)
        
        # Étape 4: Mettre à jour les flots
        for v, u in path:
            flow[v][u] += path_flow
            flow[u][v] -= path_flow
            total_cost += path_flow * costs[v][u]
        
        total_flow += path_flow
    
    return total_cost, flow