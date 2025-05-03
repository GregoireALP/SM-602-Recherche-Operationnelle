import sys
from file_parser import read_graph_file
from ford_fulkerson import ford_fulkerson
from push_relabel import push_relabel
from min_cost_flow import min_cost_flow
from utils import print_flow_matrix
from utils import print_cost_matrix

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
                
            filename = f"test{problem_num}.txt"
            graph_type, n, capacities, costs = read_graph_file(filename)
            
            if choice == "1":
                print("\nAlgorithmes pour flot maximal:")
                print("1. Ford-Fulkerson")
                print("2. Pousser-Réétiqueter")
                algo_choice = input("Choix: ")
                
                if algo_choice == "1":
                    max_flow, flow_matrix = ford_fulkerson(n, capacities)
                    
                    print("=== Résultat de Ford-Fulkerson ===")
                    print(f"\nFlot maximal: {max_flow}")
                    print("Matrice de flot:")
                    print_flow_matrix(flow_matrix, capacities)
                    
                elif algo_choice == "2":
                    max_flow, flow_matrix = push_relabel(n, capacities)
                    
                    print("=== Résultat de Pousser-Réétiqueter ===")
                    print(f"\nFlot maximal: {max_flow}")
                    print("Matrice de flot:")
                    print_flow_matrix(flow_matrix, capacities)
                    
            elif choice == "2":
                if graph_type != "min_cost":
                    print("Ce problème n'a pas de coûts associés.")
                    continue
                
                target_flow = int(input("Flot cible: "))
                total_cost, flow_matrix = min_cost_flow(n, capacities, costs, target_flow)
                
                print("=== Résultat de Flot à Coût Minimal ===")
                print(f"Coût minimal: {total_cost}")
                
                print("Matrice de flot:")
                print_flow_matrix(flow_matrix, capacities)
                
                print("Matrice de coût:")
                print_cost_matrix(costs)
                
            elif choice == "3":
                break;           
                
                
        except ValueError:
            print("Entrée invalide. Veuillez réessayer.")
        except FileNotFoundError:
            print("Fichier non trouvé. Veuillez vérifier le numéro du problème.")
        except Exception as e:
            print(f"Une erreur est survenue: {str(e)}")

if __name__ == "__main__":
    main()