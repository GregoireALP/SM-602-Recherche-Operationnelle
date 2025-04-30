import sys
from file_parser import read_graph_file
from ford_fulkerson import ford_fulkerson
from push_relabel import push_relabel
from min_cost_flow import min_cost_flow

def main():
    print("Projet de Recherche Opérationnelle - Problèmes de Flot")
    
    while True:
        print("\nMenu principal:")
        print("1. Résoudre un problème de flot maximal")
        print("2. Résoudre un problème de flot à coût minimal")
        print("3. Quitter")
        
        choice = input("Choix: ")
        
        if choice == "3":
            break
            
        try:
            problem_num = int(input("Numéro du problème (1-10): "))
            if problem_num < 1 or problem_num > 10:
                raise ValueError
                
            filename = f"test.txt"
            graph_type, n, capacities, costs = read_graph_file(filename)
            
            if choice == "1":
                print("\nAlgorithmes pour flot maximal:")
                print("1. Ford-Fulkerson")
                print("2. Pousser-Réétiqueter")
                algo_choice = input("Choix: ")
                
                if algo_choice == "1":
                    max_flow, flow_matrix = ford_fulkerson(n, capacities)
                    print(f"\nFlot maximal: {max_flow}")
                    print("Matrice de flot:")
                    print_flow_matrix(flow_matrix, capacities)
                elif algo_choice == "2":
                    max_flow, flow_matrix = push_relabel(n, capacities)
                    print(f"\nFlot maximal: {max_flow}")
                    print("Matrice de flot:")
                    print_flow_matrix(flow_matrix, capacities)
                    
            elif choice == "2":
                if graph_type != "min_cost":
                    print("Ce problème n'a pas de coûts associés.")
                    continue
                    
                max_flow, _ = ford_fulkerson(n, capacities)
                target_flow = max_flow // 2
                print(f"\nCalcul du flot à coût minimal pour une valeur de {target_flow}")
                
                total_cost, flow_matrix = min_cost_flow(n, capacities, costs, target_flow)
                print(f"Coût total: {total_cost}")
                print("Matrice de flot:")
                print_flow_matrix(flow_matrix, capacities)
                
        except ValueError:
            print("Entrée invalide. Veuillez réessayer.")
        except FileNotFoundError:
            print("Fichier non trouvé. Veuillez vérifier le numéro du problème.")
        except Exception as e:
            print(f"Une erreur est survenue: {str(e)}")

def print_flow_matrix(flow_matrix, capacities):
    n = len(flow_matrix)
    # En-tête
    print("   " + " ".join(f"{i:5}" for i in range(n)))
    # Lignes
    for i in range(n):
        print(f"{i:2} ", end="")
        for j in range(n):
            if capacities[i][j] > 0:
                print(f"{flow_matrix[i][j]:2}/{capacities[i][j]:<3}", end=" ")
            else:
                print("  0    ", end=" ")
        print()

if __name__ == "__main__":
    main()