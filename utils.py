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
        
        
from collections import deque

def bfs(residual_graph, n, s, t, parent):
    """
    Effectue une recherche en largeur (BFS) pour trouver un chemin augmentant dans le graphe résiduel.
    Affiche à chaque étape les prédécesseurs et les noeuds visités.
    """
    visited = [False] * n
    queue = deque([s])
    visited[s] = True
    
    print(f"Début de la recherche BFS depuis le sommet {s}")
    
    while queue:
        u = queue.popleft()
        print(f"Visite du sommet {u}")
        
        # Liste des successeurs accessibles
        successors = []
        
        for v in range(n):
            if not visited[v] and residual_graph[u][v] > 0:  # Si le noeud n'est pas visité et qu'il y a de la capacité résiduelle
                queue.append(v)
                visited[v] = True
                parent[v] = u
                successors.append(v)
                
                if v == t:  # Si on atteint le puits, on arrête la recherche
                    print(f"Chemin trouvé jusqu'au puits {t}")
                    return True
        
        print(f"Successeurs accessibles depuis {u} : {successors}")
    
    print("Aucun chemin augmentant trouvé")
    return False


def generer_fichiers_trace(groupe, equipe):
    """
    Génère les fichiers de trace pour les algorithmes selon les consignes de nommage.
    Les 5 premiers fichiers sont pour FF et PR, les 4 derniers pour MIN.
    
    Arguments :
    - groupe : str, le groupe (ex : "I")
    - equipe : int, le numéro de l'équipe (ex : 4)
    - probleme : int, le numéro du problème (ex : 5)
    """
    # Algorithmes et leurs suffixes
    algorithmes = {
        "Ford-Fulkerson": "FF",
        "pousser-réétiqueter": "PR",
        "flot à coût min": "MIN"
    }
    
    # Générer les fichiers pour les 10 instances
    for i in range(1, 11):  # 10 fichiers
        if i <= 5:  # Les 5 premiers fichiers pour FF et PR
            algos_a_generer = {k: v for k, v in algorithmes.items() if v in ["FF", "PR"]}
        elif i >= 7:  # Les 4 derniers fichiers pour MIN
            algos_a_generer = {k: v for k, v in algorithmes.items() if v == "MIN"}
        else:
            continue  # Ignorer le fichier 6 (aucun algo à générer)
        
        for algo, suffixe in algos_a_generer.items():
            # Construire le nom du fichier
            nom_fichier = f"{groupe}{equipe}-trace{i}-{suffixe}.txt"
            
            # Créer et écrire dans le fichier
            with open("./out/" + nom_fichier, "w") as fichier:
                fichier.write(f"Trace d'exécution pour {algo} - Instance {i}\n")
                fichier.write(f"Groupe {groupe} - Équipe {equipe} - Problème {i}\n")
                fichier.write(f"Algorithme : {algo}\n")
                fichier.write(f"Instance : {i}\n")
                fichier.write("=== Début de la trace ===\n")
                
                fichier.write("=== Fin de la trace ===\n")
    
    print("Fichiers de trace générés avec succès.")
    
    