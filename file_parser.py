def read_graph_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    
    # Détection du type de problème
    if len(lines) == 1 + 2 * int(lines[0]):
        graph_type = "min_cost"
        print("Problème de coût minimal détecté.")
    else:
        graph_type = "max_flow"
        print("Problème de flot maximal détecté.")
    
    n = int(lines[0])
    capacities = []
    costs = []
    
    # Lire les capacités
    for i in range(1, n+1):
        row = list(map(int, lines[i].split()))
        capacities.append(row)
    
    # Lire les coûts si c'est un problème de coût minimal
    if graph_type == "min_cost":
        for i in range(n+1, 2*n+1):
            row = list(map(int, lines[i].split()))
            costs.append(row)
    else:
        # Pour les problèmes de flot max sans coûts, initialiser une matrice de coûts nulle
        costs = [[0]*n for _ in range(n)]
    
    return graph_type, n, capacities, costs