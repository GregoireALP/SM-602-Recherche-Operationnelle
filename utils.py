from collections import deque

def print_flow_matrix(flow_matrix, capacities):
    n = len(flow_matrix)
    
    # Calculer les largeurs maximales nécessaires pour chaque colonne
    max_widths = [5] * n  # Largeur minimale par défaut
    
    for j in range(n):
        for i in range(n):
            if capacities[i][j] > 0:
                cell_content = f"{flow_matrix[i][j]}/{capacities[i][j]}"
                max_widths[j] = max(max_widths[j], len(cell_content))
    
    # Afficher l'en-tête
    header = "   " + " ".join(f"{i:^{max_widths[j]}}" for j, i in enumerate(range(n)))
    print(header)
    
    # Afficher les lignes de données
    for i in range(n):
        row_str = f"{i:2} "
        for j in range(n):
            if capacities[i][j] > 0:
                cell_content = f"{flow_matrix[i][j]}/{capacities[i][j]}"
                row_str += f"{cell_content:^{max_widths[j]}} "
            else:
                row_str += f"{'0':^{max_widths[j]}} "
        print(row_str)
        
       
def print_bellman_ford_matrice(distance, parent, n):
    """
    Affiche la matrice de Bellman-Ford avec pour chaque itération la distance minimale et le prédécesseur sous forme de tableau.
    """
    print("\n=== Résultat algorithme de Bellman-Ford ===")
    
    print("Distance minimale depuis la source :")
    for i in range(n):
        print(f"Sommet {i}: {distance[i]}")
    print("\nPrédécesseurs :")
    for i in range(n):
        if parent[i] != -1:
            print(f"Sommet {i}: Prédécesseur {parent[i]}")
        else:
            print(f"Sommet {i}: Pas de prédécesseur")

        
def print_cost_matrix(cost_matrix):
    """
    Affiche la matrice des coûts de manière formatée.
    
    Arguments :
    - cost_matrix : liste 2D, matrice des coûts.
    """
    n = len(cost_matrix)
    
    # Calculer les largeurs maximales nécessaires pour chaque colonne
    max_widths = [5] * n  # Largeur minimale par défaut
    
    for j in range(n):
        for i in range(n):
            if cost_matrix[i][j] > 0:
                max_widths[j] = max(max_widths[j], len(str(cost_matrix[i][j])))
    
    # Afficher l'en-tête
    header = "   " + " ".join(f"{i:^{max_widths[j]}}" for j, i in enumerate(range(n)))
    print(header)
    
    # Afficher les lignes de données
    for i in range(n):
        row_str = f"{i:2} "
        for j in range(n):
            if cost_matrix[i][j] > 0:
                cell_content = str(cost_matrix[i][j])
                row_str += f"{cell_content:^{max_widths[j]}} "
            else:
                row_str += f"{'0':^{max_widths[j]}} "
        print(row_str)
        
from collections import deque

def bfs(residual_graph, n, s, t, parent):
    """
    Effectue une recherche en largeur (BFS) pour trouver un chemin augmentant dans le graphe résiduel.
    Affiche à chaque étape les prédécesseurs et les noeuds visités.
    """
    visited = [False] * n
    queue = deque([s])
    visited[s] = True
    
    print(f"[*] Parcours en largeur à partir de la source:")
    
    while queue:
        u = queue.popleft()
        print(f"    - Visite du sommet {u}:")
        
        # Liste des successeurs accessibles
        successors = []
        
        for v in range(n):
            if not visited[v] and residual_graph[u][v] > 0:  # Si le noeud n'est pas visité et qu'il y a de la capacité résiduelle
                queue.append(v)
                visited[v] = True
                parent[v] = u
                successors.append(v)
                
                if v == t:  # Si on atteint le puits, on arrête la recherche
                    print(f"[*]Chemin améliorant trouvé")
                    return True
        
        print(f"        ->Successeurs accessibles depuis {u} : {successors}")
    
    print("[*] Aucun chemin augmentant trouvé")
    return False
