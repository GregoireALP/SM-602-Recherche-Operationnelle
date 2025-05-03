from utils import print_flow_matrix
from utils import print_cost_matrix
from utils import print_bellman_ford_matrice

def min_cost_flow(n, capacities, costs, target_flow):
    # Initialisation
    flow = [[0] * n for _ in range(n)]
    total_flow = 0
    total_cost = 0
    iteration = 0
    print("=== Initialisation ===")
    print("[*] Flot cible :" + str(target_flow))
    print("Matrice de flot initiale :")
    print_flow_matrix(flow, capacities)
    print("Matrice de coût initiale :")
    print_cost_matrix(costs)
    
    while total_flow < target_flow:
        
        print("\n=== Itération " + str(iteration) + "===")
        
        # Étape 1: Trouver le chemin de coût minimal avec Bellman-Ford
        print("Matrice de flot :")
        print_flow_matrix(flow, capacities)
        
        print("")
        
        print("Matrice de capacité:")
        print_cost_matrix(costs)
        
        print("")
        
        distance, parent = bellman_ford(n, capacities, costs, flow, 0)
        
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
        
        iteration += 1
    
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

    print_bellman_ford_matrice(distance, parent, n)
    
    return distance, parent