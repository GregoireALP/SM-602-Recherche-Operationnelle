from utils import print_flow_matrix

def min_cost_flow(n, capacities, costs):
    """
    Trouve le flot de coût minimal dans un graphe donné.
    
    Arguments :
    - n : int, nombre de sommets dans le graphe.
    - capacities : liste 2D, matrice des capacités entre les sommets.
    - costs : liste 2D, matrice des coûts entre les sommets.
    
    Retourne :
    - total_cost : int, coût total du flot.
    - flow : liste 2D, matrice représentant le flot entre les sommets.
    """
    # Initialisation
    flow = [[0] * n for _ in range(n)]
    total_flow = 0
    total_cost = 0
    
    print("=== Initialisation ===")
    
    while True:
        # Étape 1: Trouver le chemin de coût minimal avec Bellman-Ford
        distance, parent = bellman_ford(n, capacities, costs, flow, 0)
        print_flow_matrix(flow, capacities)
                
        # Si aucun chemin améliorant n'est trouvé, on arrête
        if distance[n-1] == float('inf'):
            break
        
        # Étape 2: Trouver le flot maximal sur ce chemin
        path_flow = float('inf')
        u = n-1
        while u != 0:
            v = parent[u]
            path_flow = min(path_flow, capacities[v][u] - flow[v][u])
            u = v
        
        # Étape 3: Mettre à jour les flots et calculer le coût total
        u = n-1
        while u != 0:
            v = parent[u]
            flow[v][u] += path_flow
            flow[u][v] -= path_flow
            total_cost += path_flow * costs[v][u]
            u = v
        
        total_flow += path_flow
    
    return total_cost, flow


def bellman_ford(n, capacities, costs, flow, source):
    """
    Implémente l'algorithme de Bellman-Ford pour trouver le chemin de coût minimal.
    
    Arguments :
    - n : int, nombre de sommets.
    - capacities : liste 2D, matrice des capacités.
    - costs : liste 2D, matrice des coûts.
    - flow : liste 2D, matrice des flots actuels.
    - source : int, sommet source.
    
    Retourne :
    - distance : liste, distances minimales depuis la source.
    - parent : liste, tableau des parents pour reconstruire le chemin.
    """
    distance = [float('inf')] * n
    parent = [-1] * n
    distance[source] = 0
    
    for _ in range(n-1):
        for u in range(n):
            for v in range(n):
                if capacities[u][v] - flow[u][v] > 0 and distance[v] > distance[u] + costs[u][v]:
                    distance[v] = distance[u] + costs[u][v]
                    parent[v] = u
    print("Distances minimales depuis la source :")
    for i in range(n):
        print(f"Sommet {i}: {distance[i]}")
    return distance, parent